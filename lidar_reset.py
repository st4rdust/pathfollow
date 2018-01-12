"""Restarts rplidar scanner by starting it up and then stopping it again."""

from rplidar import RPLidar
lidar = RPLidar('/dev/rplidar')
lidar.stop()
lidar.stop_motor()
lidar.disconnect()
