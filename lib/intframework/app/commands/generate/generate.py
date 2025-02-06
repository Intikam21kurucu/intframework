import os
import sys
import subprocess
import argparse
from pathlib import Path
import encoders  # Encoders.py'yi import ediyoruz
from colorama import init, Fore

# Colorama'yı başlat
init(autoreset=True)

bannergen="""
  ___  ____  _  _  ____  ____    __   ____  ____   
 / __)( ___)( \( )( ___)(  _ \  /__\ (_  _)( ___)  
( (_-. )__)  )  (  )__)  )   / /(__)\  )(   )__)   
 \___/(____)(_)\_)(____)(_)\_)(__)(__)(__) (____)
                       From -intframework-
"""

def ensure_directory_exists(directory):
    """
    Verilen dizinin var olup olmadığını kontrol eder, yoksa oluşturur.
    """
    Path(directory).mkdir(parents=True, exist_ok=True)

def apply_encoder(payload_code, encoder_type):
    """
    Encoder'ı seçilen türde uygular. Bu, payload'ı şifrelemek için kullanılabilir.
    """
    if encoder_type:
        print(f"{Fore.YELLOW}[+] Applying encoder: {encoder_type}")
        encoded_payload = encoders.encode(payload_code, encoder_type)  # Encoders.py'deki encode fonksiyonunu kullanıyoruz.
        return encoded_payload
    return payload_code

def replace_payload_placeholders(payload_code, params):
    """
    Payload'da belirtilen yer tutucuları (Lhost, Lport, Rhost, Rport) verilen parametrelerle değiştirir.
    """
    for param, value in params.items():
        placeholder = f"<{param}>"
        payload_code = payload_code.replace(placeholder, value)
    return payload_code

def convert_to_exe(input_file, output_dir, encoder_type=None, params=None):
    """
    Python dosyasını .exe formatına dönüştürür (PyInstaller kullanarak).
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            payload_code = file.read()

        # Encoder uygula (eğer varsa)
        payload_code = apply_encoder(payload_code, encoder_type)

        # Yer tutucuları (Lhost, Lport, Rhost, Rport) değiştir
        if params:
            payload_code = replace_payload_placeholders(payload_code, params)
        
        temp_file = "temp_payload.py"
        with open(temp_file, "w", encoding="utf-8") as file:
            file.write(payload_code)
        
        command = f"pyinstaller --onefile --distpath {output_dir} --workpath .build {temp_file}"
        subprocess.run(command, check=True, shell=True)
        exe_file = Path(output_dir) / f"{Path(input_file).stem}.exe"
        if exe_file.exists():
            print(f"{Fore.GREEN}[+] EXE payload generated: {exe_file}")
        else:
            print(f"{Fore.RED}[!] Error: EXE generation failed!")
    except Exception as e:
        print(f"{Fore.RED}[!] Error in converting to EXE: {e}")

def convert_to_apk(input_file, output_dir, encoder_type=None, params=None):
    """
    Python dosyasını .apk formatına dönüştürür (Buildozer kullanarak).
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            payload_code = file.read()

        # Encoder uygula (eğer varsa)
        payload_code = apply_encoder(payload_code, encoder_type)

        # Yer tutucuları (Lhost, Lport, Rhost, Rport) değiştir
        if params:
            payload_code = replace_payload_placeholders(payload_code, params)

        temp_file = "temp_payload.py"
        with open(temp_file, "w", encoding="utf-8") as file:
            file.write(payload_code)

        buildozer_command = f"buildozer android debug deploy run {temp_file}"
        subprocess.run(buildozer_command, check=True, shell=True)
        apk_file = Path(output_dir) / f"{Path(input_file).stem}.apk"
        if apk_file.exists():
            print(f"{Fore.GREEN}[+] APK payload generated: {apk_file}")
        else:
            print(f"{Fore.RED}[!] Error: APK generation failed!")
    except Exception as e:
        print(f"{Fore.RED}[!] Error in converting to APK: {e}")

def convert_to_mp4(input_file, output_dir, encoder_type=None, params=None):
    """
    Python dosyasını mp4 formatına dönüştürür (FFmpeg kullanarak).
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            payload_code = file.read()

        # Encoder uygula (eğer varsa)
        payload_code = apply_encoder(payload_code, encoder_type)

        # Yer tutucuları (Lhost, Lport, Rhost, Rport) değiştir
        if params:
            payload_code = replace_payload_placeholders(payload_code, params)

        temp_file = "temp_payload.py"
        with open(temp_file, "w", encoding="utf-8") as file:
            file.write(payload_code)

        mp4_file = Path(output_dir) / f"{Path(input_file).stem}.mp4"
        command = f"ffmpeg -loop 1 -framerate 2 -t 5 -i {temp_file} -c:v libx264 -pix_fmt yuv420p {mp4_file}"
        subprocess.run(command, check=True, shell=True)
        if mp4_file.exists():
            print(f"{Fore.GREEN}[+] MP4 file generated: {mp4_file}")
        else:
            print(f"{Fore.RED}[!] Error: MP4 generation failed!")
    except Exception as e:
        print(f"{Fore.RED}[!] Error in converting to MP4: {e}")

def convert_to_vbs(input_file, output_dir, encoder_type=None, params=None):
    """
    Python dosyasını .vbs formatına dönüştürür (Windows Script Host kullanarak).
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            payload_code = file.read()

        # Encoder uygula (eğer varsa)
        payload_code = apply_encoder(payload_code, encoder_type)

        # Yer tutucuları (Lhost, Lport, Rhost, Rport) değiştir
        if params:
            payload_code = replace_payload_placeholders(payload_code, params)

        temp_file = "temp_payload.vbs"
        with open(temp_file, "w", encoding="utf-8") as file:
            file.write(payload_code)

        vbs_file = Path(output_dir) / f"{Path(input_file).stem}.vbs"
        if Path(vbs_file).exists():
            print(f"{Fore.GREEN}[+] VBS payload generated: {vbs_file}")
        else:
            print(f"{Fore.RED}[!] Error: VBS generation failed!")
    except Exception as e:
        print(f"{Fore.RED}[!] Error in converting to VBS: {e}")

def convert_to_jar(input_file, output_dir, encoder_type=None, params=None):
    """
    Python dosyasını .jar formatına dönüştürür (PyInstaller kullanarak).
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            payload_code = file.read()

        # Encoder uygula (eğer varsa)
        payload_code = apply_encoder(payload_code, encoder_type)

        # Yer tutucuları (Lhost, Lport, Rhost, Rport) değiştir
        if params:
            payload_code = replace_payload_placeholders(payload_code, params)

        temp_file = "temp_payload.py"
        with open(temp_file, "w", encoding="utf-8") as file:
            file.write(payload_code)

        command = f"pyinstaller --onefile --distpath {output_dir} --workpath .build {temp_file}"
        subprocess.run(command, check=True, shell=True)
        jar_file = Path(output_dir) / f"{Path(input_file).stem}.jar"
        if jar_file.exists():
            print(f"{Fore.GREEN}[+] JAR payload generated: {jar_file}")
        else:
            print(f"{Fore.RED}[!] Error: JAR generation failed!")
    except Exception as e:
        print(f"{Fore.RED}[!] Error in converting to JAR: {e}")

def convert_to_ps1(input_file, output_dir, encoder_type=None, params=None):
    """
    Python dosyasını .ps1 formatına dönüştürür (PowerShell kullanarak).
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            payload_code = file.read()

        # Encoder uygula (eğer varsa)
        payload_code = apply_encoder(payload_code, encoder_type)

        # Yer tutucuları (Lhost, Lport, Rhost, Rport) değiştir
        if params:
            payload_code = replace_payload_placeholders(payload_code, params)

        temp_file = "temp_payload.ps1"
        with open(temp_file, "w", encoding="utf-8") as file:
            file.write(payload_code)

        ps1_file = Path(output_dir) / f"{Path(input_file).stem}.ps1"
        if ps1_file.exists():
            print(f"{Fore.GREEN}[+] PS1 payload generated: {ps1_file}")
        else:
            print(f"{Fore.RED}[!] Error: PS1 generation failed!")
    except Exception as e:
        print(f"{Fore.RED}[!] Error in converting to PS1: {e}")

def convert_to_wav(input_file, output_dir, encoder_type=None, params=None):
    """
    Python dosyasını .wav formatına dönüştürür (FFmpeg kullanarak).
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            payload_code = file.read()

        # Encoder uygula (eğer varsa)
        payload_code = apply_encoder(payload_code, encoder_type)

        # Yer tutucuları (Lhost, Lport, Rhost, Rport) değiştir
        if params:
            payload_code = replace_payload_placeholders(payload_code, params)

        temp_file = "temp_payload.py"
        with open(temp_file, "w", encoding="utf-8") as file:
            file.write(payload_code)

        wav_file = Path(output_dir) / f"{Path(input_file).stem}.wav"
        command = f"ffmpeg -f wav -i {temp_file} {wav_file}"
        subprocess.run(command, check=True, shell=True)
        if wav_file.exists():
            print(f"{Fore.GREEN}[+] WAV file generated: {wav_file}")
        else:
            print(f"{Fore.RED}[!] Error: WAV generation failed!")
    except Exception as e:
        print(f"{Fore.RED}[!] Error in converting to WAV: {e}")

def parse_arguments():
    """
    Argümanları alır ve işler.
    """
    parser = argparse.ArgumentParser(description="Convert Scripts")
    parser.add_argument("-i", "--input", required=True, help="Input file (e.g., payload.py).")
    parser.add_argument("-o", "--output", required=True, help="Output directory (e.g., /tmp/).")
    parser.add_argument("-f", "--format", required=True, choices=["exe", "apk", "mp4", "vbs", "jar", "ps1", "wav"], help="Output format.")
    parser.add_argument("-e", "--encoder", choices=["base64", "urlencode", "hex"], help="Optional encoder to apply.")
    parser.add_argument("-p", "--params", help="Optional parameters for Lhost, Lport, Rhost, Rport in the format Lhost=<ip> Lport=<port>.", nargs="*", default=[])

    return parser.parse_args()

def main():
    """
    Ana fonksiyon.
    """
    args = parse_arguments()

    # Parametreleri bir sözlük haline getir
    params = {}
    for param in args.params:
        key, value = param.split("=")
        params[key] = value

    # Çıktı dizinini oluştur
    ensure_directory_exists(args.output)

    # Dosya formatına göre uygun dönüşüm fonksiyonunu çağır
    if args.format == "exe":
        convert_to_exe(args.input, args.output, args.encoder, params)
    elif args.format == "apk":
        convert_to_apk(args.input, args.output, args.encoder, params)
    elif args.format == "mp4":
        convert_to_mp4(args.input, args.output, args.encoder, params)
    elif args.format == "vbs":
        convert_to_vbs(args.input, args.output, args.encoder, params)
    elif args.format == "jar":
        convert_to_jar(args.input, args.output, args.encoder, params)
    elif args.format == "ps1":
        convert_to_ps1(args.input, args.output, args.encoder, params)
    elif args.format == "wav":
        convert_to_wav(args.input, args.output, args.encoder, params)

if __name__ == "__main__":
    print(bannergen)
    main()