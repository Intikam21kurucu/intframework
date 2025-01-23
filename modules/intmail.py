#!/usr/bin/env python3
import sys
import os
import argparse
from configparser import ConfigParser
import requests
from emailrep.utils import parse_args, load_config
from emailrep import EmailRep

CONF_PATH = os.path.expanduser("~/.config/sublime")
CONF_FILE = os.path.join(CONF_PATH, "setup.cfg")
CONF_DEFAULTS = {"emailrep": {"key": ""}}

def parse_args():
    parser = argparse.ArgumentParser(
        prog='intmail',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""

""")

    parser.add_argument('query', nargs='?')
    parser.add_argument('-r', '--report', help='Email address to report',
                        action='store', dest='report', type=str, required=False)
    parser.add_argument('--tags', help='Tags that should be applied',
                        action='store', dest='tags', type=str, required=False)
    parser.add_argument('--description', help='Additional information and context',
                        action='store', dest='description', type=str, required=False)
    parser.add_argument('--timestamp', help=(
                        'When this activity occurred as a string, defaults to now(). '
                        'Example: "Sun Aug 18 22:51:32 EDT 2019" or "08/18/2019 22:51:32 EDT"'
                        ), action='store', dest='timestamp', type=str, required=False)
    parser.add_argument('--expires', help=(
                        'Number of hours the email should be considered risky'
                        ), action='store', dest='expires', type=int, required=False)
    parser.add_argument('--proxy', help=(
                        'Proxy to use for requests. Example: "socks5://10.10.10.10:8000"'
                        ), action='store', dest='proxy', type=str, required=False),

    args, unknown = parser.parse_known_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit()

    elif sys.argv[1] == "setup":
        setup()

    elif not args.report:
        return (EmailRep.QUERY, Namespace(query=sys.argv[1]), args.proxy)

    else:
        if not args.report or not args.tags:
            print("--report and --tags are required for reporting email addresses")
            sys.exit()
        return (EmailRep.REPORT, args, args.proxy)


def setup():
    if len(sys.argv) == 4 and sys.argv[2] == "-k":
        if not os.path.isfile(CONF_FILE):
            if not os.path.exists(CONF_PATH):
                os.makedirs(CONF_PATH)

        config = ConfigParser()
        config["emailrep"] = {}
        config["emailrep"]["key"] = sys.argv[3]
        with open(CONF_FILE, "w") as f:
            config.write(f)
            print("Success! ~/.config/sublime/setup.cfg file generated.")
            sys.exit()
    else:
        print(
            "Setup requires an API key.\n"
            "Usage: emailrep setup -k <api key>"
        )
        sys.exit()


def load_config():
    config = ConfigParser()
    if not os.path.isfile(CONF_FILE):
        config.read_dict(CONF_DEFAULTS)
        return config

    config.read(CONF_FILE)
    return config


class EmailRep():
    QUERY = "QUERY"
    REPORT = "REPORT"

    def __init__(self, key=None, proxy=None):
        self.base_url = BASE_URL
        self.headers = {}
        self.version = "0.0.5"
        self.headers["User-Agent"] = "python/emailrep.io v%s" % self.version
        self.headers["Content-Type"] = "application/json"

        if key:
            self.headers["Key"] = key
        self.session = requests.Session()
        if proxy:
            self.session.proxies = {"https": "{}".format(proxy)}

        self.banner = """
_____   __________  ___      _ __
   /  _/ | / /_  __/  |/  /___ _(_) /
   / //  |/ / / / / /|_/ / __ `/ / /
 _/ // /|  / / / / /  / / /_/ / / /
/___/_/ |_/ /_/ /_/  /_/\__,_/_/_/
"""

    def query(self, email):
        url = "{}/{}?summary=true".format(self.base_url, email)

        result = self.session.get(url, headers=self.headers)
        return result.json()

    def report(self, email, tags, description=None, timestamp=None, expires=None):
        url = self.base_url + "/report"
        params = {}
        params["email"] = email
        params["tags"] = tags

        if description:
            params["description"] = description

        if timestamp:
            params["timestamp"] = timestamp

        if expires:
            params["expires"] = expires

        result = self.session.post(url, json=params, headers=self.headers)
        return result.json()

    def format_query_output(self, result):
        print(self.banner)
        print("Email address: %s\n" % result["email"])
        print("\033[91mRISKY\033[0m\n") if result["suspicious"] else None
        print(result["summary"])


def main():
    (action, args, proxy) = parse_args()
    config = load_config()

    emailrep = EmailRep(
        key=config.get('emailrep', 'key'),
        proxy=proxy)

    try:
        if action == EmailRep.QUERY:
            result = emailrep.query(args.query)

            if result.get("status") and result["status"] == "fail":
                print("Failed: %s" % result["reason"])
                sys.exit()

            emailrep.format_query_output(result)

        elif action == EmailRep.REPORT:
            email = args.report
            tags = args.tags.split(",")

            if args.timestamp:
                try:
                    timestamp = parser.parse(args.timestamp)
                    timestamp = int(timestamp.timestamp())
                except Exception as e:
                    print("invalid timestamp: %s" % str(e))
                    sys.exit()
            else:
                timestamp = None

            result = emailrep.report(email, tags, args.description, timestamp, args.expires)
            if result.get("status") and result["status"] == "success":
                print("Successfully reported %s" % email)
            else:
                print("Failed to report %s. Reason: %s" % (email, result["reason"]))

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()