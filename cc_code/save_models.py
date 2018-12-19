# -*- coding:utf-8 -*-

###this script is used to mv files every 1 hour

import time
import subprocess

time_val=3600  #one hour

while True:
    time.sleep(time_val)
    subprocess.call("mv models/* dst_file", shell=True)
    print("hello world")



