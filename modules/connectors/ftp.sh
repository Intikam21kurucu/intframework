#!/bin/sh

# Get IP address from the first argument
ip=$1

# Check if IP address is provided
if [ -z "$ip" ]; then
    echo "Error: IP address not specified."
    exit 1
fi

# Connect to the specified IP address via FTP
echo "Connecting to FTP server at: $ip"
ftp $ip