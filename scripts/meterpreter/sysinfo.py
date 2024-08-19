import subprocess

class SystemChecker:
    def __init__(self, rhost):
        self.rhost = rhost

    def cmd_exec(self, command):
        try:
            result = subprocess.check_output(command, shell=True, text=True)
            return result
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            return ""

    def report_host(self, report):
        # Implement your reporting logic here
        print("Reporting host:", report)

    def get_sysinfo(self):
        system_info = {}
        
        # Execute command and split output into lines
        cmd_output = self.cmd_exec("/usr/bin/sw_vers").split("\n")
        
        for line in cmd_output:
            if ':' in line:
                field, val = line.strip().split(":", 1)
                system_info[field.strip()] = val.strip()
        
        # Get Kernel information and Hostname
        system_info["Kernel"] = self.cmd_exec("uname -a")
        system_info["Hostname"] = system_info["Kernel"].split(" ")[1]

        # Report host information
        self.report_host({
            'host': self.rhost,
            'os_name': 'osx',
            'os_flavor': system_info["Kernel"],
            'name': system_info["Hostname"]
        })

        return system_info

    def os_check(self):
        # Get sysinfo
        sysinfo = self.get_sysinfo()
        
        # Make sure it's OS X (Darwin)
        if "Darwin" not in sysinfo.get("Kernel", ""):
            self.print_warning("The target system does not appear to be running OS X!")
            self.print_warning(f"Kernel information: {sysinfo.get('Kernel', '')}")
            return
        
        # Make sure it's not greater than 10.5 or less than 9.5
        version = sysinfo.get("ProductVersion", "")
        try:
            minor_version = float(version[3:])
            if not (9.5 <= minor_version <= 10.5):
                self.print_warning("The target version of OS X does not appear to be compatible with the exploit!")
                self.print_warning(f"Target is running OS X {sysinfo.get('ProductVersion', '')}")
        except ValueError:
            self.print_warning("Unable to parse OS X version.")

    def print_warning(self, message):
        print("WARNING:", message)

# Usage example
checker = SystemChecker(rhost=None)
checker.os_check()