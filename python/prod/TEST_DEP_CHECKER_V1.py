#!/usr/bin/env python
import socket
import sys
import os
import time 
import datetime
#############CREATE VARIABLES FOR DEVICES THAT RESOLVE IN DNS ####################
depnumber = input("Enter DEP Number: ")
host2 =('DP0' + depnumber +'HVSR01.corp.fsroot.testsite.com')
host3 =('DP0' + depnumber +'HVSR01.wmgt.testsite.com')
switch1 =('SCDP0' + depnumber +'-1.dcom.testsite.com')
switch2 =('SCDP0' + depnumber +'-2.dcom.testsite.com')
printer1= ('PRT-DEP' + depnumber +'-0001.testsite.com')
printer2= ('PRT-DEP' + depnumber +'-0002.testsite.com')
printer3= ('MFD-DEP' + depnumber +'-0001.testsite.com')
hv=('DP0' + depnumber +'hv.testsite.com')
refname= socket.gethostbyname(switch1)
refname_split= refname.split('.')
lanprefix= (refname_split[0]+'.'+ refname_split[1] +'.'+ refname_split[2]+'.')

#################################PING THE DEVICES/VARIABLES CREATED ABOVE AND OUTPUT RESULTS##########    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
rep = os.system( 'ping ' + host2)
if rep == 0: 
    output=('Server is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
else:
    output=('Server is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
time.sleep(1)
print ("   ")
print ("   ")
print ("   ")
print (output)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
rep = os.system( 'ping ' + host3)
if rep == 0: 
    output=('Server mgmt connection  is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
else:
    output=('Server mgmt connection is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
time.sleep(1)
print ("   ")
print ("   ")
print ("   ")
print (output)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
rep = os.system( 'ping ' + switch1)
if rep == 0: 
    output=('Server is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
else:
    output=('Server is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
time.sleep(1)
print ("   ")
print ("   ")
print ("   ")
print (output)
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
rep = os.system( 'ping ' + switch2)
if rep == 0: 
    output=('Server is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
else:
    output=('Server is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
time.sleep(1)
print ("   ")
print ("   ")
print ("   ")
print (output)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
rep = os.system( 'ping ' + printer1)
if rep == 0: 
    output=('Printer 1 is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
else:
    output=('Printer 1 is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
time.sleep(1)
print ("   ")
print ("   ")
print ("   ")
print (output)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
rep = os.system( 'ping ' + printer2)
if rep == 0: 
    output=('Printer 2 is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
else:
    output=('Printer 2 is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
time.sleep(1)
print ("   ")
print ("   ")
print ("   ")
print (output)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
rep = os.system( 'ping ' + printer2)
if rep == 0: 
    output=('MFD Printer 1 is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
else:
    output=('MFD Printer 1 is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
time.sleep(1)
print ("   ")
print ("   ")
print ("   ")
print (output)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
rep = os.system( 'ping ' + hv)
if rep == 0: 
    output=('HV unit IP module is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
else:
    output=('HV unit IP module is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
time.sleep(1)
print ("   ")
print ("   ")
print ("   ")
print (output)

######################CREATE VARIABLES FOR DEVCIES THAT DO NOT HAVE DNS NAMES REWUIRES MANUATL INPUT############
#LAN = input("Enter LAN subnet: ")


device1 = (lanprefix + '10')
device2 = (lanprefix + '5')
device2B = (lanprefix + '48')
device3 = (lanprefix + '45')
device4 = (lanprefix + '81')
device5 = (lanprefix + '47')
device6 = (lanprefix + '49')
#################################PING THE DEVICES/VARIABLES CREATED ABOVE AND OUTPUT RESULTS##########
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
rep = os.system( 'ping ' + device1)
if rep == 0: 
    output=('Site Scan Server is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
else:
    output=('Site Scan Server is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
time.sleep(1)
print ("   ")
print ("   ")
print ("   ")
print (output)
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
rep = os.system( 'ping ' + device2)
if rep == 0: 
    output=('Wireless AP1  is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
else:
    output=('Wireless AP1 is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
time.sleep(1)
print ("   ")
print ("   ")
print ("   ")
print (output)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
rep = os.system( 'ping ' + device2B)
if rep == 0: 
    output=('Printer 1  is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
else:
    output=('Printer 1 is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
time.sleep(1)
print ("   ")
print ("   ")
print ("   ")
print (output)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
rep = os.system( 'ping ' + device3)
if rep == 0: 
    output=('DVR is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
else:
    output=('DVR is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
time.sleep(1)
print ("   ")
print ("   ")
print ("   ")
print (output)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
rep = os.system( 'ping ' + device4)
if rep == 0: 
    output=('ATM1 is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
else:
    output=('ATM1 is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
time.sleep(1)
print ("   ")
print ("   ")
print ("   ")
print (output)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
rep = os.system( 'ping ' + device5)
if rep == 0: 
    output=('Printer 2 is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
else:
    output=('Printer 2 is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
time.sleep(1)
print ("   ")
print ("   ")
print ("   ")
print (output)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
rep = os.system( 'ping ' + device6)
if rep == 0: 
    output=('MFD Printer is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
else:
    output=('MFD Printer  is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
	    
time.sleep(1)
print ("   ")
print ("   ")
print ("   ")
print (output)
