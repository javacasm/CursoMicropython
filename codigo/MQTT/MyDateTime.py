import machine
import ntptime
import utime

# from Utils import identifyModule

# DateTime utility

v = '1.4.2'
moduleName = 'MyDateTime'

'''
def setRTC():
    ntptime.settime()
    return getLocalTimeHumanFormat()
'''
def getLocalTimeHumanFormat():
    strLocalTime = "{0}/{1:02}/{2:02} {3:02}:{4:02}:{5:02}".format(*utime.localtime(utime.time())[0:6])
    return strLocalTime

def test_MyDateTime():
    sDate = getLocalTimeHumanFormat()
    print(sDate + ' Module ' + moduleName + ' ' + v)
