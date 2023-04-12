import math

import rdrive as rr

class Servo:
    def __init__(self, name_interface, name_id, logger):
        print(name_interface)
        logger.info("Initializing ServoApi")
        self.api = rr.ServoApi()

        logger.info("Initializing interface {}".format(name_interface))
        self.interface_init = self.api.init_interface(name_interface)

        logger.info("Initializing servo id {}".format(name_id))
        self.servo = self.interface_init.init_servo(name_id)

        logger.info("Setting servo to operational state")
        self.servo.set_state_operational()

    def _init_api(self):
        pass

    def start(self, per, logger):
        logger.info("Start")

        dict = {
            1: [60., 5800],
            2: [120., 3000],
            3: [240., 1700]
        }
        self.servo.set_position(360.)

        # установить конкретную скорость (градусы/сек)
        self.servo.set_velocity(dict[per][0])  # 120 #240 #60

        # сон
        self.api.sleep_ms(3000 * 2)

    def stop(self):
        self.servo.set_state_stopped()
