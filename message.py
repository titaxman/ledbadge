#!/usr/bin/python
import os
import subprocess
import sys
import time

import badge

DEVICE = subprocess.check_output('ls /dev/ttyUSB*', shell=True)
DEVICE = DEVICE[0:12]
MESSAGE = sys.argv[1]
SPEED = sys.argv[2]
ACTION = sys.argv[3]

os.system("stty speed 38400 <" + DEVICE + ">/dev/null")
f = open(DEVICE, "w")
pkts = badge.build_packets(0x600, badge.message_file(MESSAGE, speed=SPEED, action=ACTION))
for p in pkts:
    f.write(p.format())
f.flush()
f.close()
