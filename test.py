import logging
import os
import argparse
import threading
import rdrive as rr
import Interface
from servo import Servo

logging.basicConfig()
logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--servo_1_id", type=int, help="first servo ID that you want control"
)
parser.add_argument("--interface", type=str, help="interface name")
print("GO")

args = parser.parse_args()

INTERFACE_NAME = args.interface
SERVO_1_ID = args.servo_1_id

Interface.interface(INTERFACE_NAME, SERVO_1_ID, logger)





