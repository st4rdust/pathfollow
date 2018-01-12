# !/usr/bin/env python3
"""Records measurments to a given file."""

import sys
from rplidar import RPLidar
import time


PORT_NAME = '/dev/rplidar'


def lidarToFile(path):
    """Do the actual thing."""
    lidar = RPLidar(PORT_NAME)
    lidar.set_pwm(322)
    time.sleep(5)
    outfile = open(path, 'w')
    try:
        print('Recording measurments... Press Crl+C to stop.')
        for measurement in lidar.iter_measurments():
            line = '\t'.join(str(v) for v in measurement)
            outfile.write(line + '\n')
    except KeyboardInterrupt:
        print('Stopping.')
    lidar.stop()
    lidar.disconnect()
    outfile.close()


if __name__ == '__main__':
    if (len(sys.argv) == 0):
        filelocation = sys.path[0] + "/lidar.txt"
    else:
        filelocation = sys.argv[1]
    print(filelocation)
    lidarToFile(filelocation)
