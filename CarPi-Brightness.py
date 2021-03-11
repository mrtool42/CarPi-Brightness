
import time
import pytz
from datetime import datetime
from astral import Astral
from os import system

a = Astral()
city = a['Vienna']
now = datetime.now(pytz.utc)
sun = city.sun(date=now, local=True)

dawn = sun['dawn']
dusk = sun['dusk']

system("sudo pigpiod")

if now > dawn and now < dusk:
    system("pigs p 18 255")
#    print("day")
    
else:
    system("pigs p 18 30")
#    print("night")