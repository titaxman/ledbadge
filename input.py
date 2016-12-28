#!/usr/bin/python
import os
import subprocess
import sys
import time
import string

import badge

DEVICE = subprocess.check_output('ls /dev/ttyUSB*', shell=True)
DEVICE = DEVICE[0:12]
MESSAGE = raw_input("Enter message (max 250 chars): ")
SPEED = raw_input("Enter Speed (1-5): ")
ACTION = raw_input("What action? (A,B,C,D,E): ")

os.system("stty speed 38400 <" + DEVICE + ">/dev/null")
f = open(DEVICE, "w")
pkts = badge.build_packets(0x600, badge.message_file(MESSAGE, speed=SPEED, action=ACTION))

for p in pkts:
    f.write(p.format())
f.flush()
f.close()
