import argparse
import nmap
from nmap3 import nmap3 as nmap3_api

def perform_nmap_scan(target, args):
    nm = nmap.PortScanner()
    scan_args = []

    # Timing and Performance
    if args.scan_delay:
        scan_args.append(f'--scan-delay {args.scan_delay}')
    if args.max_scan_delay:
        scan_args.append(f'--max-scan-delay {args.max_scan_delay}')
    if args.min_rate:
        scan_args.append(f'--min-rate {args.min_rate}')
    if args.max_rate:
        scan_args.append(f'--max-rate {args.max_rate}')
    if args.timing_template:
        scan_args.append(f'-T {args.timing_template}')

    # Firewall/IDS Evasion and Spoofing
    if args.firewall_evasion:
        scan_args.append(f'--firewall-evasion {args.firewall_evasion}')
    if args.mtu:
        scan_args.append(f'--mtu {args.mtu}')
    if args.decoy:
        scan_args.append(f'-D {args.decoy}')
    if args.spoof_source:
        scan_args.append(f'-S {args.spoof_source}')
    if args.interface:
        scan_args.append(f'-e {args.interface}')
    if args.source_port:
        scan_args.append(f'-g {args.source_port}')
    if args.proxies:
        scan_args.append(f'--proxies {args.proxies}')
    if args.data:
        scan_args.append(f'--data {args.data}')
    if args.data_string:
        scan_args.append(f'--data-string {args.data_string}')
    if args.data_length:
        scan_args.append(f'--data-length {args.data_length}')
    if args.ip_options:
        scan_args.append(f'--ip-options {args.ip_options}')
    if args.ttl:
        scan_args.append(f'--ttl {args.ttl}')
    if args.spoof_mac:
        scan_args.append(f'--spoof-mac {args.spoof_mac}')
    if args.badsum:
        scan_args.append('--badsum')

    # Output
    if args.output_normal:
        scan_args.append(f'-oN {args.output_normal}')
    if args.output_xml:
        scan_args.append(f'-oX {args.output_xml}')
    if args.output_grepable:
        scan_args.append(f'-oG {args.output_grepable}')
    if args.output_all:
        scan_args.append(f'-oA {args.output_all}')
    if args.verbosity:
        scan_args.append(f'-v {args.verbosity}')
    if args.debug:
        scan_args.append('-d')
    if args.reason:
        scan_args.append('--reason')
    if args.open:
        scan_args.append('--open')
    if args.packet_trace:
        scan_args.append('--packet-trace')
    if args.iflist:
        scan_args.append('--iflist')
    if args.append_output:
        scan_args.append('--append-output')
    if args.resume:
        scan_args.append(f'--resume {args.resume}')
    if args.noninteractive:
        scan_args.append('--noninteractive')

    # Perform the scan with nmap
    result = nm.scan(hosts=target, arguments=' '.join(scan_args))
    return result

def perform_nmap3_scan(target, args):
    nmap3 = nmap3_api.Nmap()
    scan_args = {}

    # Timing and Performance
    if args.scan_delay:
        scan_args['scan_delay'] = args.scan_delay
    if args.max_scan_delay:
        scan_args['max_scan_delay'] = args.max_scan_delay
    if args.min_rate:
        scan_args['min_rate'] = args.min_rate
    if args.max_rate:
        scan_args['max_rate'] = args.max_rate
    if args.timing_template:
        scan_args['timing_template'] = args.timing_template

    # Firewall/IDS Evasion and Spoofing
    if args.firewall_evasion:
        scan_args['firewall_evasion'] = args.firewall_evasion
    if args.mtu:
        scan_args['mtu'] = args.mtu
    if args.decoy:
        scan_args['decoy'] = args.decoy
    if args.spoof_source:
        scan_args['spoof_source'] = args.spoof_source
    if args.interface:
        scan_args['interface'] = args.interface
    if args.source_port:
        scan_args['source_port'] = args.source_port
    if args.proxies:
        scan_args['proxies'] = args.proxies
    if args.data:
        scan_args['data'] = args.data
    if args.data_string:
        scan_args['data_string'] = args.data_string
    if args.data_length:
        scan_args['data_length'] = args.data_length
    if args.ip_options:
        scan_args['ip_options'] = args.ip_options
    if args.ttl:
        scan_args['ttl'] = args.ttl
    if args.spoof_mac:
        scan_args['spoof_mac'] = args.spoof_mac
    if args.badsum:
        scan_args['badsum'] = args.badsum

    # Output
    if args.output_normal:
        scan_args['output_normal'] = args.output_normal
    if args.output_xml:
        scan_args['output_xml'] = args.output_xml
    if args.output_grepable:
        scan_args['output_grepable'] = args.output_grepable
    if args.output_all:
        scan_args['output_all'] = args.output_all
    if args.verbosity:
        scan_args['verbosity'] = args.verbosity
    if args.debug:
        scan_args['debug'] = args.debug
    if args.reason:
        scan_args['reason'] = args.reason
    if args.open:
        scan_args['open'] = args.open
    if args.packet_trace:
        scan_args['packet_trace'] = args.packet_trace
    if args.iflist:
        scan_args['iflist'] = args.iflist
    if args.append_output:
        scan_args['append_output'] = args.append_output
    if args.resume:
        scan_args['resume'] = args.resume
    if args.noninteractive:
        scan_args['noninteractive'] = args.noninteractive

    # Perform the scan with nmap3
    result = nmap3.scan_top_ports(target)
    return result

def main():
    parser = argparse.ArgumentParser(prog="nmap", description="nmap [options]")

    # Target Specification
    parser.add_argument('target', type=str, nargs='?', default=None, help='Target IP or hostname')

    # Timing and Performance
    parser.add_argument('--timing-template', type=int, choices=range(0, 6), help='Timing template (0-5)')
    parser.add_argument('--scan-delay', type=str, help='Delay between probes')
    parser.add_argument('--max-scan-delay', type=str, help='Maximum delay between probes')
    parser.add_argument('--min-rate', type=int, help='Minimum packet send rate')
    parser.add_argument('--max-rate', type=int, help='Maximum packet send rate')

    # Firewall/IDS Evasion and Spoofing
    parser.add_argument('--firewall-evasion', type=str, help='Firewall/IDS evasion techniques')
    parser.add_argument('--mtu', type=int, help='Set the MTU for network packets')
    parser.add_argument('--decoy', type=str, help='Use decoy addresses for scan')
    parser.add_argument('--spoof-source', type=str, help='Spoof source address')
    parser.add_argument('--interface', type=str, help='Network interface to use')
    parser.add_argument('--source-port', type=int, help='Set source port for scans')
    parser.add_argument('--proxies', type=str, help='Use these proxies for scanning')
    parser.add_argument('--data', type=str, help='Send arbitrary data in scan packets')
    parser.add_argument('--data-string', type=str, help='Send arbitrary data string in scan packets')
    parser.add_argument('--data-length', type=int, help='Send data with specified length')
    parser.add_argument('--ip-options', type=str, help='Set IP options')
    parser.add_argument('--ttl', type=int, help='Set IP Time-To-Live')
    parser.add_argument('--spoof-mac', type=str, help='Spoof MAC address')
    parser.add_argument('--badsum', action='store_true', help='Send packets with bad checksums')

    # Output
    parser.add_argument('--output-normal', type=str, help='Save results in normal format')
    parser.add_argument('--output-xml', type=str, help='Save results in XML format')
    parser.add_argument('--output-grepable', type=str, help='Save results in grepable format')
    parser.add_argument('--output-all', action='store_true', help='Save all output formats')
    parser.add_argument('--verbosity', type=int, choices=range(0, 10), help='Set verbosity level')
    parser.add_argument('--debug', action='store_true', help='Enable debug output')
    parser.add_argument('--reason', action='store_true', help='Show reason for port state')
    parser.add_argument('--open', action='store_true', help='Show open ports only')
    parser.add_argument('--packet-trace', action='store_true', help='Show all packets sent and received')
    parser.add_argument('--iflist', action='store_true', help='Show network interfaces and routing table')
    parser.add_argument('--append-output', action='store_true', help='Append to output file instead of overwriting')
    parser.add_argument('--resume', type=str, help='Resume an aborted scan from a file')
    parser.add_argument('--noninteractive', action='store_true', help='Disable interactive prompts')

    args = parser.parse_args()

    print(f"Performing scan on target: {args.target}")

    # Perform nmap scan
    nmap_result = perform_nmap_scan(args.target, args)
    print("Nmap Scan Results:")
    print(nmap_result)

    # Perform nmap3 scan
    nmap3_result = perform_nmap3_scan(args.target, args)
    print("Nmap3 Scan Results:")
    print(nmap3_result)

if __name__ == "__main__":
    main()