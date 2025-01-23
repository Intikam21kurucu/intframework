import argparse
from pyroute2 import IPRoute

def add_route(destination, gateway):
    """Add a route to the routing table."""
    try:
        with IPRoute() as ipr:
            # Add the route
            ipr.route('add', dst=destination, gateway=gateway)
            print(f"Route to {destination} via {gateway} added successfully.")
    except Exception as e:
        print(f"Error adding route: {e}")

def delete_route(destination):
    """Delete a route from the routing table."""
    try:
        with IPRoute() as ipr:
            # Delete the route
            ipr.route('del', dst=destination)
            print(f"Route to {destination} deleted successfully.")
    except Exception as e:
        print(f"Error deleting route: {e}")

def list_routes():
    """List all routes in the routing table."""
    try:
        with IPRoute() as ipr:
            routes = ipr.get_routes()
            print("Current routing table:")
            for route in routes:
                print(f"Destination: {route['dst']}, Gateway: {route.get('gateway', 'N/A')}")
    except Exception as e:
        print(f"Error listing routes: {e}")

def update_route(old_destination, new_destination, new_gateway):
    """Update an existing route in the routing table."""
    try:
        with IPRoute() as ipr:
            # Find and delete the old route
            ipr.route('del', dst=old_destination)
            print(f"Old route to {old_destination} deleted.")

            # Add the new route
            ipr.route('add', dst=new_destination, gateway=new_gateway)
            print(f"Route updated to {new_destination} via {new_gateway}.")
    except Exception as e:
        print(f"Error updating route: {e}")

def main():
    parser = argparse.ArgumentParser(description="Manage network routes using pyroute2.")
    parser.add_argument('-a', '--add', nargs=2, metavar=('DEST', 'GATEWAY'), help="Add a route. Example: -a 192.168.2.0/24 192.168.2.1")
    parser.add_argument('-d', '--delete', metavar='DEST', help="Delete a route. Example: -d 192.168.2.0/24")
    parser.add_argument('-l', '--list', action='store_true', help="List all routes in the routing table.")
    parser.add_argument('-u', '--update', nargs=3, metavar=('OLD_DEST', 'NEW_DEST', 'NEW_GATEWAY'), help="Update an existing route. Example: -u 192.168.2.0/24 192.168.3.0/24 192.168.3.1")

    args = parser.parse_args()

    if args.add:
        add_route(args.add[0], args.add[1])
    elif args.delete:
        delete_route(args.delete)
    elif args.list:
        list_routes()
    elif args.update:
        update_route(args.update[0], args.update[1], args.update[2])
    else:
        parser.print_help()

if __name__ == "__main__":
    main()