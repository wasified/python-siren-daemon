#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lifel
#
# Created:     30/04/2023
# Copyright:   (c) lifel 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import psutil
import time
import datetime
from playsound import playsound


def alert():
    playsound('siren.mp3')

while True:
    time.sleep(0.1)
    now = datetime.datetime.now()
    print(now.time())
    plugged_in = psutil.sensors_battery().power_plugged
    if not plugged_in:
        print ("Laptop is plugged out.")
        alert()
        #played = True
        break
    print ("Laptop was plugged in till: %s"%now)


