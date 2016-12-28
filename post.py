#!/usr/bin/python
import os
import sys
import subprocess

import badge

DEVICE = subprocess.check_output('ls /dev/ttyUSB*', shell=True)
DEVICE = DEVICE[0:12]

os.system("stty speed 38400 <" + DEVICE + ">/dev/null")
f = open(DEVICE, "w")
pkts = badge.build_packets(0x600, badge.message_file(sys.argv[1], speed='1', action=badge.ACTION_HOLD))
for p in pkts:
    f.write(p.format())
f.flush()
f.close()
