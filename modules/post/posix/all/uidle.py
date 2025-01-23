import ctypes
import os
import time
import argparse
import psutil
from ctypes.util import find_library

# XScreenSaverInfo Structure
class XScreenSaverInfo(ctypes.Structure):
    _fields_ = [
        ('window', ctypes.c_ulong),   # screen saver window
        ('state', ctypes.c_int),      # off, on, disabled
        ('kind', ctypes.c_int),       # blanked, internal, external
        ('since', ctypes.c_ulong),    # milliseconds
        ('idle', ctypes.c_ulong),     # milliseconds
        ('event_mask', ctypes.c_ulong) # events
    ]

# Initialize variables
xlib = None
xss = None
xlibs_available = None

XOpenDisplay = None
XDefaultRootWindow = None
XCloseDisplay = None
XFree = None
XScreenSaverAllocInfo = None
XScreenSaverQueryInfo = None

def load_uidle_libs():
    """Load necessary libraries for accessing display and screen saver info."""
    global xlib, xss
    global XOpenDisplay, XDefaultRootWindow, XCloseDisplay
    global XFree, XScreenSaverAllocInfo, XScreenSaverQueryInfo
    global xlibs_available

    if xlibs_available is not None:
        return

    try:
        xlib = ctypes.cdll.LoadLibrary(find_library('X11'))

        XOpenDisplay = xlib.XOpenDisplay
        XOpenDisplay.argtypes = [ctypes.c_char_p]
        XOpenDisplay.restype = ctypes.c_void_p

        XDefaultRootWindow = xlib.XDefaultRootWindow
        XDefaultRootWindow.argtypes = [ctypes.c_void_p]
        XDefaultRootWindow.restype = ctypes.c_ulong

        XCloseDisplay = xlib.XCloseDisplay
        XCloseDisplay.argtypes = [ctypes.c_void_p]
        XCloseDisplay.restype = ctypes.c_int

        XFree = xlib.XFree
        XFree.argtypes = [ctypes.c_void_p]
        XFree.restype = ctypes.c_int

    except:
        xlib = None

    try:
        xss = ctypes.cdll.LoadLibrary('libXss.so.1')

        XScreenSaverAllocInfo = xss.XScreenSaverAllocInfo
        XScreenSaverAllocInfo.restype = ctypes.POINTER(XScreenSaverInfo)

        XScreenSaverQueryInfo = xss.XScreenSaverQueryInfo
        XScreenSaverQueryInfo.argtypes = [
            ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p
        ]
        XScreenSaverQueryInfo.restype = ctypes.c_int

    except:
        xss = None

    if xlib and xss:
        xlibs_available = True

def get_gui_idle(display=None):
    """Get idle time based on GUI activity (X11)."""
    if not os.environ.get('DISPLAY'):
        return None

    load_uidle_libs()

    if xlibs_available is False:
        return None

    display = XOpenDisplay(os.environ.get('DISPLAY'))
    if not display:
        return None

    xssinfo = XScreenSaverAllocInfo()
    if not xssinfo:
        XCloseDisplay(display)
        return None

    idle = None

    status = XScreenSaverQueryInfo(display, XDefaultRootWindow(display), xssinfo)
    if status:
        idle = xssinfo.contents.idle
        XFree(xssinfo)

    XCloseDisplay(display)

    return int(idle / 1000) if idle else None

def get_cli_idle():
    """Get idle time based on terminal activity."""
    now = time.time()

    idles = []
    for user in psutil.users():
        if not user.terminal:
            continue

        try:
            dev_stat = os.stat('/dev/' + user.terminal)
        except OSError:
            continue

        idles.append(now - dev_stat.st_atime)

    if not idles:
        return None

    idle = min(idles)
    psutil._pmap = {}
    return idle

def get_idle(method="auto"):
    """Get the idle time based on specified method."""
    cli_idle = get_cli_idle()

    try:
        gui_idle = get_gui_idle()
    except:
        gui_idle = None

    if method == "cli":
        return cli_idle
    elif method == "gui":
        return gui_idle
    elif method == "auto":
        if gui_idle is None:
            return cli_idle
        elif cli_idle is None:
            return gui_idle
        else:
            return min(cli_idle, gui_idle)
    else:
        return None

def main():
    """Main function to parse arguments and display idle time."""
    parser = argparse.ArgumentParser(description="Get system idle time.")
    parser.add_argument(
        '--method', choices=['auto', 'cli', 'gui'], default='auto',
        help="Method to get idle time ('auto' chooses the best available method)"
    )
    parser.add_argument(
        '--verbose', action='store_true', help="Enable verbose output"
    )
    args = parser.parse_args()

    idle_time = get_idle(args.method)
    
    if args.verbose:
        print(f"Idle time retrieved using method: {args.method}")
        if idle_time is not None:
            print(f"Idle time: {idle_time:.2f} seconds")
        else:
            print("Could not retrieve idle time.")
    else:
        if idle_time is not None:
            print(f"{idle_time:.2f}")
        else:
            print("Could not retrieve idle time.")

if __name__ == "__main__":
    main()