import os
import sys


def isup(ip):
    if sys.platform == "win32":
        pingstring = "ping -n 2 {} > NUL".format(ip)
    else:
        pingstring = "ping -c 2 {} > /dev/null".format(ip)
    result = os.system(pingstring)
    if result == 0:
        return True
    else:
        return False

def isup1(ip):
    if sys.platform == "win32":
        pingstring = "ping -n 2 {} > NUL".format(ip)
    else:
        pingstring = "ping -c 2 {} > /dev/null".format(ip)
    result = os.system(pingstring)
    if result == 0:
        return ip,True
    else:
        return ip,False
