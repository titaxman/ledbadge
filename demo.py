#!/usr/bin/python
import os
import subprocess
import time

import badge

DEVICE = subprocess.check_output('ls /dev/ttyUSB*', shell=True)
DEVICE = DEVICE[0:12]
MESSAGE = "Python"

os.system("stty speed 38400 <" + DEVICE + ">/dev/null")
f = open(DEVICE, "w")
pkts = badge.build_packets(0x600, badge.message_file(MESSAGE, speed='5', action=badge.ACTION_HOLD))
for p in pkts:
    f.write(p.format())
f.flush()
f.close()
