from rplidar import RPLidar
lidar=RPLidar('/dev/rplidar')
lidar.stop()
lidar.stop_motor()
lidar.disconnect()
