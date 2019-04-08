import picamera
import time
import numpy as np

class MyOutput(object):
    def __init__(self):
        self.size = 0
        self.timestamps = []
        self.last_time = time.time()

    def write(self, s):
        self.size += len(s)
        img = np.frombuffer(s, np.uint8, 640*480)
        self.timestamps.append(time.time()-self.last_time)
        self.last_time = time.time()

    def flush(self):
        speed = np.array(self.timestamps)
        print(speed.mean(), speed.std())


with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 100
    camera.start_recording(MyOutput(), format='yuv')
    camera.wait_recording(10)
    camera.stop_recording()
