import platform
import psutil
import socket

def get_system_info():
    info = {}

    # İşletim sistemi bilgisi
    info['os'] = "İNTİKAM21'S DESKTOP"
    info['os_version'] = platform.version()
    info['os_release'] = platform.release()

    # Donanım bilgisi
    info['architecture'] = platform.machine()
    info['processor'] = platform.processor()
    info['cpu_cores'] = psutil.cpu_count(logical=True)
    info['cpu_physical_cores'] = psutil.cpu_count(logical=False)
    info['memory'] = psutil.virtual_memory().total

    # Ağ bilgisi
    info['hostname'] = socket.gethostname()
    info['ip_address'] = socket.gethostbyname(info['hostname'])

    # Disk bilgisi
    disk_usage = psutil.disk_usage('/')
    info['total_disk_space'] = disk_usage.total
    info['used_disk_space'] = disk_usage.used
    info['free_disk_space'] = disk_usage.free

    return info

if __name__ == '__main__':
    system_info = get_system_info()
    for key, value in system_info.items():
        if key in ['memory', 'total_disk_space', 'used_disk_space', 'free_disk_space']:
            value = f"{value / (1024**3):.2f} GB"
        print(f'{key}: {value}')