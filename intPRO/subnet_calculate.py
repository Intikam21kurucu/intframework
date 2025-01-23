import ipaddress
from colorama import Fore, Style

def subnet_calculator(ip_network):
    try:
        network = ipaddress.IPv4Network(ip_network, strict=False)
        return network
    except ValueError as e:
        return f"{Fore.RED}Error: {e}{Style.RESET_ALL}"

def subnet_calculator_module():
    print(f"{Fore.GREEN}Subnet Calculator Module Started!{Style.RESET_ALL}")
    
    while True:
        module = input(f"{Fore.RED + Style.BRIGHT}int4{Style.RESET_ALL} PRO({Fore.RED + Style.BRIGHT}SubnetCalculator{Style.RESET_ALL}) > ")
        
        if module.lower() == "exit":
            print(f"{Fore.YELLOW}Exiting the module...{Style.RESET_ALL}")
            break
        
        elif module.startswith("calculate "):
            try:
                _, ip_network = module.split(" ")
                network = subnet_calculator(ip_network)
                if isinstance(network, ipaddress.IPv4Network):
                    print(f"{Fore.YELLOW}Network: {network.network_address}, Netmask: {network.netmask}, Broadcast: {network.broadcast_address}{Style.RESET_ALL}")
                else:
                    print(network)
            except ValueError:
                print(f"{Fore.RED}Invalid input! Correct usage: calculate <IP/Netmask>{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED} usage: calculate <IP/Netmask>{Style.RESET_ALL}")
if __name__ == "__main__" or "main":
	subnet_calculator_module()