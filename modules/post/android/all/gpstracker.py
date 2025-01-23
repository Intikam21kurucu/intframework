import requests
from jnius import autoclass, cast
from plyer import gps
from time import sleep
import os
import datetime
from threading import Thread
import jnius

# Global variables
GPSTRACKER_THREAD = None
TRACES = []
CURRENT_LAT, CURRENT_LON = None, None

# Global location setter
def __getLocation__(**kwargs):
    '''Updates the GPS location.'''
    global CURRENT_LAT, CURRENT_LON
    if kwargs:
        CURRENT_LAT = kwargs.get('lat')
        CURRENT_LON = kwargs.get('lon')
        # Show updated location on the terminal
        print(f"[INFO] New location: Latitude: {CURRENT_LAT}, Longitude: {CURRENT_LON}")

class GpsTracker(Thread):
    def __init__(self, period=15, inMemory=False):
        '''Initializes the GPS tracker.'''
        Thread.__init__(self)
        gps.configure(on_location=__getLocation__)
        self.stopFollow = False
        self.period = period
        self.inMemory = inMemory
        self.filename = "gps_tracking.csv"
        self.Context = autoclass('android.content.Context')
        self.PythonActivity = autoclass('org.renpy.android.PythonService')
        self.LocationManager = autoclass('android.location.LocationManager')

    def enable(self):
        '''Starts GPS tracking.'''
        gps.start()

    def disable(self):
        '''Stops GPS tracking.'''
        gps.stop()

    def stop(self):
        '''Stops the GPS tracker.'''
        self.stopFollow = True

    def isGPSenabled(self):
        '''Checks if GPS is enabled.'''
        locationManager = cast('android.location.LocationManager', self.PythonActivity.mService.getSystemService(self.Context.LOCATION_SERVICE))
        isGPSEnabled = locationManager.isProviderEnabled(self.LocationManager.GPS_PROVIDER)
        return isGPSEnabled

    def isNetworkProviderEnabled(self):
        '''Checks if Network Provider is enabled.'''
        locationManager = cast('android.location.LocationManager', self.PythonActivity.mService.getSystemService(self.Context.LOCATION_SERVICE))
        isNetworkProviderEnabled = locationManager.isProviderEnabled(self.LocationManager.NETWORK_PROVIDER)
        return isNetworkProviderEnabled

    def getCurrentLocation(self):
        '''Returns current GPS coordinates.'''
        global CURRENT_LAT, CURRENT_LON
        return CURRENT_LAT, CURRENT_LON

    def follow(self):
        '''Starts tracking location and prints data periodically.'''
        global TRACES
        self.enable()
        lastLat, lastLon = None, None
        if not self.inMemory:
            if not os.path.isfile(self.filename):
                f = open(self.filename, 'w')
                f.write("date,latitude,longitude\n")
                f.close()
        while not self.stopFollow:
            lat, lon = self.getCurrentLocation()
            if (lat is not None and lon is not None) and (lastLat != lat or lastLon != lon):
                if not self.inMemory:
                    f = open(self.filename, 'a+')
                    f.write("{0},{1},{2}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), lat, lon))
                    f.close()
                else:
                    TRACES.append([datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), lat, lon])
                # Print data to the terminal
                print(f"[INFO] Location updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} | Lat: {lat} | Lon: {lon}")
            lastLat, lastLon = lat, lon
            sleep(self.period)
        self.disable()
        jnius.detach()  # Fix for issue with PyJNIus

    def run(self):
        '''Runs the GPS tracker in a separate thread.'''
        self.stopFollow = False
        self.follow()

    def isFollowing(self):
        '''Checks if GPS tracking is still active.'''
        return not self.stopFollow

def startGpsTracker(period):
    '''Starts the GPS tracking thread.'''
    global GPSTRACKER_THREAD
    if GPSTRACKER_THREAD is None or not GPSTRACKER_THREAD.isFollowing():
        gpsTracker = GpsTracker(period=period)
        gpsTracker.start()
        GPSTRACKER_THREAD = gpsTracker
        return True
    else:
        return False

def stopGpsTracker():
    '''Stops the GPS tracker thread.'''
    global GPSTRACKER_THREAD
    if GPSTRACKER_THREAD is None or not GPSTRACKER_THREAD.isFollowing():
        return False
    else:
        GPSTRACKER_THREAD.stop()
        GPSTRACKER_THREAD.join()
        return True

def dumpGpsTracker():
    '''Returns the trace data when inMemory mode is enabled.'''
    global TRACES
    return TRACES

def statusGpsTracker():
    '''Checks the status of the GPS tracker.'''
    global GPSTRACKER_THREAD
    return GPSTRACKER_THREAD is not None and GPSTRACKER_THREAD.isFollowing()

def deleteFile():
    '''Deletes the tracking file if GPS tracking is stopped.'''
    if GPSTRACKER_THREAD is not None and not GPSTRACKER_THREAD.isFollowing():
        try:
            os.remove(GPSTRACKER_THREAD.filename)
        except OSError:
            return False
        return True
    return False