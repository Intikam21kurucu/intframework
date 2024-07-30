from setuptools import setup, find_packages

setup(
    name="inttable",
    version="4.0.0.1",
    description="FRAMEWORK",
    url="https://github.com/Intikam21kurucu/intframework",
    packages=find_packages(),
    author="intikam21",
    author_email="intikam21app@gmail.com",
    license="GPL-3.0",
    install_requires=[
        "shodan", "requests", "prompt_toolkit", "wget", "beautifulsoup4", 
        "click", "urllib3", "IP2proxy", "h8mail",
        "pythonping", "whois", "netaddr", "pillow", "tweepy", 
        "pyfiglet"
    ],
    scripts=[
        'intconsoleV4.py', "intcrawler.py", "usersearcher.py", 
        "imei.py", "exploit_searcher.py", "expdatabase.py", 
        "modules/evasionint.py", "modules/intmodules.py", "modules/phonesearcher.py", 
        "modules/shodan.py", "modules/shotgun.py", "modules/imei.py", 
        "modules/intninja.py", "modules/meterpreter_user.py", "modules/meterpreter.py", 
        "modules/intmeterpreter.py"
    ],
    entry_points={
        'console_scripts': [
            'intconsole=intconsoleV4:main',  # intconsoleV4.py'daki main fonksiyonuna başvuruyor
        ],
    },
)