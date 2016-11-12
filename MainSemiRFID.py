#!/usr/bin/python

import nfc
import mysql
#import thread
import time
import RPi.GPIO as GPIO
from decimal import Decimal
MASTER_TAG = "861492187281" #MASTER TAG FOR ADD OR DELETE
TimeOutBank = 0

def readTagID():
    cardId=nfc.readNfc()
    beep()
    print("readTagID...")
    return cardId

def ledRedOn():
    GPIO.output(6,False)

def ledRedOff():
    GPIO.output(6,True)

def beep():
    GPIO.output(5,False)
    time.sleep(0.1)
    GPIO.output(5,True)

def beep_on():
    GPIO.output(5,False)

def beep_off():
    GPIO.output(5,True)

def initGpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    ledRedOff()
    time.sleep(0.1)
    beep()
    time.sleep(0.1)
    beep()
#    time.sleep(0.1)
#    beep()

def SetTimeOut():
    TimeOut = time.strftime("%S", time.localtime())
    TimeOut = (int(Decimal(self.TimeOut))) - 1
    TimeOut += 30
    if TimeOut > 59:
        TimeOut -= 59
    if TimeOut < 10:
        TimeOut = "0" + str(TimeOut)
    else:
        TimeOut = str(TimeOut)
    print ("TimeOut : " + str(TimeOut))

def main():
    GPIO.cleanup()
    try:
        initGpio()
        while True:
            print (" SEMI RPi RFID \n")
            print (" *** READY *** \n")
            cardId2 = readTagID()
            print ("TAG Card Number: "+ str(cardId2))
            StatusTag = mysql.ReadTagID(cardId2)
            if StatusTag != 0:
                print ("----Welcome---- \n")
                mysql.ReadName(cardId2)
                ledRedOn()
                beep_on()
                time.sleep(2.0)
                ledRedOff()
                beep_off()
            else:
                beep()
                print ("--Not allowed-- \n")
            time.sleep(2.0)
    except KeyboardInterrupt:
        GPIO.cleanup()
        pass
    GPIO.cleanup()

if __name__ == '__main__':
    main()
