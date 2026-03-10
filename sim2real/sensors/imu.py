# sim2real/sensors/imu.py

import time 

from config import load_yaml
# from mpu9250_jmdev.registers import *
# from mpu9250_jmdev.mpu_9250 import MPU9250

imu_cfg = load_yaml('config/imu.yaml')

class IMUReader:
    def __init__(self):
        pass