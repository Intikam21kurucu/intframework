from pyroute2 import IPRoute
import argparse

def add_tunnel(local_ip, remote_ip, local_tunnel_ip, remote_tunnel_ip):
    """Add a tunnel interface to route traffic over."""
    try:
        with IPRoute() as ipr:
            # Add tunnel interface
            ipr.link('add', ifname='tun0', kind='tun')
            # Bring the tunnel up
            ipr.link('set', index=ipr.link_lookup(ifname='tun0')[0], state='up')
            # Add IP addresses to the tunnel interface
            ipr.addr('add', index=ipr.link_lookup(ifname='tun0')[0], address=local_tunnel_ip, mask=24)
            ipr.addr('add', index=ipr.link_lookup(ifname='tun0')[0], address=remote_tunnel_ip, mask=24)
            # Add routes for the tunnel
            ipr.route('add', dst='0.0.0.0/0', gateway=remote_ip, oif=ipr.link_lookup(ifname='tun0')[0])
            print(f"Tunnel interface 'tun0' created and configured successfully.")
    except Exception as e:
        print(f"Error adding tunnel: {e}")

def delete_tunnel():
    """Delete the tunnel interface."""
    try:
        with IPRoute() as ipr:
            # Find tunnel interface index
            tun_index = ipr.link_lookup(ifname='tun0')[0]
            # Delete IP addresses
            ipr.addr('del', index=tun_index, address='0.0.0.0/0')
            # Delete tunnel interface
            ipr.link('del', index=tun_index)
            print("Tunnel interface 'tun0' deleted successfully.")
    except Exception as e:
        print(f"Error deleting tunnel: {e}")

def gather_device_info():
    """Gather network information from the device connected via the tunnel."""
    try:
        with IPRoute() as ipr:
            # Get routing table
            routes = ipr.get_routes()
            print("Routing table:")
            for route in routes:
                print(f"Destination: {route['dst']}, Gateway: {route.get('gateway', 'N/A')}")
            
            # Get network interfaces and their IPs
            interfaces = ipr.get_links()
            print("Network interfaces:")
            for interface in interfaces:
                print(f"Interface: {interface['ifname']}, IP: {interface.get('address', 'N/A')}")
    except Exception as e:
        print(f"Error gathering device info: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage network tunnels and gather device information using pyroute2.")
    parser.add_argument('-a', '--add', nargs=4, metavar=('LOCAL_IP', 'REMOTE_IP', 'LOCAL_TUNNEL_IP', 'REMOTE_TUNNEL_IP'), help="Add a tunnel. Example: -a 192.168.1.2 192.168.1.1 10.0.0.1 10.0.0.2")
    parser.add_argument('-d', '--delete', action='store_true', help="Delete the tunnel interface.")
    parser.add_argument('-g', '--gather', action='store_true', help="Gather network information from the device connected via the tunnel.")

    args = parser.parse_args()

    if args.add:
        add_tunnel(args.add[0], args.add[1], args.add[2], args.add[3])
    elif args.delete:
        delete_tunnel()
    elif args.gather:
        gather_device_info()
    else:
        parser.print_help()