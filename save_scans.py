#!/usr/bin/env python3
"""
Records scans to a given file in the form of numpy array.

Usage example:
$ ./record_scans.py out.npy
"""
import sys
import numpy as np
import time
from rplidar import RPLidar


PORT_NAME = '/dev/rplidar'


def run(path):
    """Do the actual thing when the file is run."""
    lidar = RPLidar(PORT_NAME)
    time.sleep(5)
    data = []
    try:
        print("Recording scans... Press Ctrl+C to stop.")
        for scan in lidar.iter_scans():
            if (len(scan) <= 164):
                data.append(np.array(scan))
    except KeyboardInterrupt:
        print("Stopping.")
    lidar.stop()
    lidar.disconnect()
    del data[0]
    np.save(path, np.array(data))


if __name__ == '__main__':
    run(sys.argv[1])
