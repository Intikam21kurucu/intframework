import dns.resolver
from colorama import Fore, Style

def dns_zone_transfer(domain):
    try:
        answers = dns.resolver.resolve(domain, 'AXFR')
        return answers
    except dns.resolver.NoAnswer:
        return None
    except dns.resolver.NXDOMAIN:
        return f"{Fore.RED}Domain does not exist.{Style.RESET_ALL}"
    except Exception as e:
        return f"{Fore.RED}Error: {e}{Style.RESET_ALL}"

def dns_zone_transfer_module():
    print(f"{Fore.GREEN}DNS Zone Transfer Test Module Started!{Style.RESET_ALL}")
    
    while True:
        module = input(f"{Fore.RED + Style.BRIGHT}int4{Style.RESET_ALL} PRO({Fore.RED}DNSZoneTransfer{Style.RESET_ALL}) > ")
        
        if module.lower() == "exit":
            print(f"{Fore.YELLOW}Exiting the module...{Style.RESET_ALL}")
            break
        
        elif module.startswith("test "):
            try:
                _, domain = module.split(" ")
                transfer_info = dns_zone_transfer(domain)
                if transfer_info:
                    print(f"{Fore.YELLOW}DNS Zone Transfer data: {transfer_info}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}No Zone Transfer available or DNS query failed.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input! Correct usage: test <domain>{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid command: {module}{Style.RESET_ALL}")
if __name__ == "__main__" or "main":
	dns_zone_transfer_module()