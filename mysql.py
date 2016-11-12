#-------------------------------------------------------------------------------
# Name:        MySQL reader/writer
# Purpose:
#
# Author:      Jakub 'Yim' Dvorak
#
# Created:     26.10.2013
# Copyright:   (c) Jakub Dvorak 2013
# Licence:
#   ----------------------------------------------------------------------------
#   "THE BEER-WARE LICENSE" (Revision 42):
#   Jakub Dvorak wrote this file. As long as you retain this notice you
#   can do whatever you want with this stuff. If we meet some day, and you think
#   this stuff is worth it, you can buy me a beer in return.
#   ----------------------------------------------------------------------------
#-------------------------------------------------------------------------------
import MySQLdb
import time
from decimal import Decimal
#from time import strftime,localtime
#import datetime
#from unidecode import unidecode

def connect():
    # Mysql connection setup. Insert your values here
    return MySQLdb.connect(host="localhost", user="root", passwd="486210", db="FHON")

def ReadTagID(IdCard):
    db = connect()
    curs=db.cursor()

    curs.execute ("SELECT * FROM raspberrypi WHERE id_card=%s", (str(IdCard)))
    count = 0
    readid = []
    for readid in curs.fetchall():
        count = count+1
#            print "TadID: "+ str(readid[2])+"   "+\
#                    "Password: "+ str(readid[3])
#    time.sleep(0.2)
    db.close()

    if count > 0:
        return readid[0]
    else:
        count = None
        return 0


def ReadName(cardId):
    db = connect()
    curs=db.cursor()

    curs.execute ("SELECT Name FROM raspberrypi WHERE id_card=%s", (str(IdCard)))
    Name2 = curs.fetchone()
    print (Name2)
    db.close()
