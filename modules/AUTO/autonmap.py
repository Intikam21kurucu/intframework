#!/usr/bin/env python

try:
    import time
    from libnmap.process import NmapProcess
    from libnmap.parser import NmapParser, NmapParserException
except Exception as e:
    print('\n[!] Failed imports: %s \n' % str(e))


class AutoNmap:
    def __init__(self, targetSet, clientName, nmapOptions):
        self.options = nmapOptions
        self.clientName = clientName
        self.targetList = list(targetSet)

    def scan_tcp(self):
        print('[i] Running nmap scan against %s hosts' % len(self.targetList))

        for i, t in enumerate(self.targetList):
            print('[i] Scanning host %s of %s : %s with options %s' % (i + 1, len(self.targetList), t, self.options))

            parsed = None
            nmproc = NmapProcess(t, ''.join(self.options))
            rc = nmproc.run()
            if rc != 0:
                print("nmap scan failed: {0}".format(nmproc.stderr))
                continue

            try:
                parsed = NmapParser.parse(nmproc.stdout)
            except NmapParserException as e:
                print("Exception raised while parsing scan: {0}".format(e.msg))
                continue

            self.print_scan(parsed)

    def scan_udp(self):
        print('[i] Running nmap scan against %s targets' % len(self.targetList))

        nmap_proc = NmapProcess(targets=self.targetList, options="-n -sU -T4 --min-hostgroup=50")
        nmap_proc.run_background()
        while nmap_proc.is_running():
            print("Nmap Scan running: ETC: {0} DONE: {1}%".format(nmap_proc.etc, nmap_proc.progress))
            time.sleep(10)

        print("rc: {0} output: {1}".format(nmap_proc.rc, nmap_proc.summary))

    def print_scan(self, parsed):
        if not parsed:
            print("No parsed results to print.")
            return

        print("Starting Nmap {0} ( http://nmap.org ) at {1}".format(parsed.version, parsed.started))

        for host in parsed.hosts:
            if len(host.hostnames):
                tmp_host = host.hostnames.pop()
            else:
                tmp_host = host.address

            print("Nmap scan report for {0} ({1})".format(tmp_host, host.address))
            print("Host is {0}.".format(host.status))
            print("  PORT     STATE         SERVICE")

            for serv in host.services:
                pserv = "{0:>5s}/{1:3s}  {2:12s}  {3}".format(str(serv.port), serv.protocol, serv.state, serv.service)
                if len(serv.banner):
                    pserv += " ({0})".format(serv.banner)
                print(pserv)
        print(parsed.summary)


def main():
    targets = ["127.0.0.1"]  # Example target, replace with actual targets
    client_name = "ClientName"
    nmap_options = "-T4 -p- -sV"

    runNmap = AutoNmap(targets, client_name, nmap_options)
    runNmap.scan_tcp()  # Run a TCP scan


if __name__ == '__main__':
    main()