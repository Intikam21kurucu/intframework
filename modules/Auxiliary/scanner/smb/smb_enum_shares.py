import os
import smbclient
import subprocess
from sys import argv


def create_directory(path):
    """ Creates a directory; does nothing if it already exists. """
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        print(f"Error creating directory {path}: {e}")


def download_and_test_upload_SMB(share_connection, remote_SMB_server, share_name):
    """ Downloads files from an SMB share and performs an upload test. """

    try:
        smb_shared_dirs = ["/"]

        for folder in smb_shared_dirs:
            try:
                for item in share_connection.listdir(folder):
                    item_path = f"{folder}{item}/"
                    if share_connection.exists(item_path):
                        smb_shared_dirs.append(item_path)
            except smbclient.SambaClientError as e:
                print(f"Error listing folder {folder}: {e}")

        # Create base directory
        base_dir = f"{remote_SMB_server}-SMB/{share_name}"
        create_directory(base_dir)

        for folder in smb_shared_dirs:
            create_directory(f"{base_dir}/{folder}")

            # Test file upload
            try:
                share_connection.upload("test_upload_SMB.txt", f"{folder}/test_upload_SMB.txt")
                print(f"Successfully uploaded test file to {folder} in SMB share {share_name} on server {remote_SMB_server}!")
            except smbclient.SambaClientError:
                print(f"Failed to upload test file to {folder} in SMB share {share_name} on server {remote_SMB_server}")

            # Downloading files
            for item in share_connection.listdir(folder):
                try:
                    if folder != "/":
                        share_connection.download(f"{folder}{item}", f"{base_dir}/{folder}/{item}")
                    else:
                        share_connection.download(f"{folder}{item}", f"{base_dir}/{item}")
                except smbclient.SambaClientError:
                    print(f"Downloading folder {item} from SMB server {remote_SMB_server}...")

        return True
    except smbclient.SambaClientError:
        return False


def main():
    if len(argv) == 2:
        SMB_server = argv[1]
        SMB_username = ""
        SMB_password = ""
    elif len(argv) == 4:
        SMB_server = argv[1]
        SMB_username = argv[2]
        SMB_password = argv[3]
    else:
        print("Usage: python3 smb_enumeration.py SMB_server [ SMB_username SMB_password ]")
        exit(0)

    # LIST SMB SHARES
    if SMB_username == "":
        smbclient_output = subprocess.getstatusoutput(f"/usr/bin/smbclient -L {SMB_server} -N")
    else:
        # Create authentication file
        with open(f"authfileSMB-{SMB_server}", "w") as authfile:
            authfile.write(f"username = {SMB_username}\npassword = {SMB_password}\n")

        smbclient_output = subprocess.getstatusoutput(f"/usr/bin/smbclient -L {SMB_server} -A authfileSMB-{SMB_server}")
        os.remove(f"authfileSMB-{SMB_server}")

    if smbclient_output[0] == 1:
        print(f"Unable to list SMB shares for server {SMB_server} without credentials.")
        exit(0)

    smb_output_lines = smbclient_output[1].split("\n")[3:]

    if SMB_username == "":
        print(f"Here are the SMB shares on server {SMB_server} visible without credentials:")
    else:
        print(f"Here are the SMB shares on server {SMB_server} visible with the account {SMB_username}:")

    SMB_shares = [line.split()[0] for line in smb_output_lines if "Disk" in line]

    print(SMB_shares)

    create_directory(f"{SMB_server}-SMB")

    with open("test_upload_SMB.txt", "w") as test_file:
        test_file.write("Test file upload to SMB server.")

    if SMB_username == "":
        # Connect to SMB shares without credentials
        for share in SMB_shares:
            smb_conn = smbclient.SambaClient(server=SMB_server, share=share, username="anonymous", password="")
            if not download_and_test_upload_SMB(smb_conn, SMB_server, share):
                smb_conn = smbclient.SambaClient(server=SMB_server, share=share, username="", password="")
                if not download_and_test_upload_SMB(smb_conn, SMB_server, share):
                    print(f"Unable to connect to SMB share {share} on server {SMB_server} without credentials.")
    else:
        # Connect to SMB shares with credentials
        for share in SMB_shares:
            smb_conn = smbclient.SambaClient(server=SMB_server, share=share, username=SMB_username, password=SMB_password)
            if not download_and_test_upload_SMB(smb_conn, SMB_server, share):
                print(f"Unable to connect to SMB share {share} on server {SMB_server} with account {SMB_username}.")

    print(f"All accessible SMB shares on server {SMB_server} have been downloaded to the folder {SMB_server}-SMB")
    os.remove("test_upload_SMB.txt")


if __name__ == "__main__":
    main()