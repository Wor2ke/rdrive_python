import rdrive as rr


class ServoMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances


class Servo(metaclass=ServoMeta):

    def __init__(self, name_interface, name_id, logger):
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
        # установка позиции (градусы/обр)
        self.servo.set_position(360.)

        # установить конкретную скорость (градусы/сек)
        self.servo.set_velocity(dict[per][0])  # 120 #240 #60

        # сон
        self.api.sleep_ms(3000 * 2)

    def get_velocity(self):
        self.servo.param_cache_setup_entry(rr.APP_PARAM_VELOCITY, True)
        self.servo.param_cache_update()
        return self.servo.read_cached_parameter(rr.APP_PARAM_VELOCITY)

    def get_voltage(self):
        self.servo.param_cache_setup_entry(rr.APP_PARAM_VOLTAGE_INPUT, True)
        self.servo.param_cache_update()
        return self.servo.read_cached_parameter(rr.APP_PARAM_VOLTAGE_INPUT)

    def get_temperature(self):
        self.servo.param_cache_setup_entry(rr.APP_PARAM_TEMPERATURE_ELECTRONICS, True)
        self.servo.param_cache_update()
        return self.servo.read_cached_parameter(rr.APP_PARAM_TEMPERATURE_ELECTRONICS)

    def get_amper(self):
        self.servo.param_cache_setup_entry(rr.APP_PARAM_CURRENT_PHASE, True)
        self.servo.param_cache_update()
        return self.servo.read_cached_parameter(rr.APP_PARAM_CURRENT_PHASE)

    def stop(self):
        logger.info("Stop")
        # заморозка сервопривода
        self.servo.freeze()
