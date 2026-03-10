# sim2real/motor/motor_controller.py

import numpy as np

from .motor_registers import *


class MotorController:
    def __init__(self, cfg):
        self._cfg = cfg
        
        # Initialize PortHandler instance
        self.portHandler = PortHandler(self._cfg["port"])

        # Initialize PacketHandler instance
        self.packetHandler = PacketHandler(self._cfg["protocol_version"])

        # Initialize GroupSyncRead


        # port open
        self.port_open()

        # torque enable
        self.torque_on(self._cfg["motor_ids"])

    def port_open(self):
        if self.portHandler.open():
            print("Succeeded to open the port")
        else:
            print("Failed to open the port")
        
        if self.portHandler.setBaudRate(self._cfg["baudrate"]):
            print("Succeeded to change the baudrate")
        else:
            print("Failed to change the baudrate")

    def torque_on(self, motor_ids: list[int]):
        for motor_id in motor_ids:
            dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(
                self.portHandler,
                motor_id,
                self.cfg["ADDR_TORQUE_ENABLE"],
                self._cfg["TORQUE_ENABLE"]
                )
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % self.packetHandler.getRxPacketError(dxl_error))
            else:
                print("Dynamixel#%d has been successfully connected" % motor_id)

    def action_apply(self, action: np.ndarray):
        pass