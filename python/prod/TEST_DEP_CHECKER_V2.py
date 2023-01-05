#!/usr/bin/env python
import socket
import sys
import os
import time 
import datetime
#############CREATE VARIABLES FOR DEVICES THAT RESOLVE IN DNS ####################
depnumber = input("Enter DEP Number: ")
ds=('.testsite.com')
host2 =('DP0' + depnumber +'HVSR01.corp.fsroot'+ds)
host3 =('DP0' + depnumber +'HVSR01.wmgt'+ds)
switch1 =('SCDP0' + depnumber +'-1.dcom'+ds)
switch2 =('SCDP0' + depnumber +'-2.dcom'+ds)
printer1= ('PRT-DEP' + depnumber +'-0001'+ds)
printer2= ('PRT-DEP' + depnumber +'-0002'+ds)
printer3= ('MFD-DEP' + depnumber +'-0001'+ds)
hv=('DP0' + depnumber +'hv'+ds)
refname= socket.gethostbyname(switch1)
refname_split= refname.split('.')
lanprefix= (refname_split[0]+'.'+ refname_split[1] +'.'+ refname_split[2]+'.')
device1 = (lanprefix + '10')
device2 = (lanprefix + '5')
device2b = (lanprefix + '48')
device3 = (lanprefix + '45')
device4 = (lanprefix + '81')
device5 = (lanprefix + '47')
device6 = (lanprefix + '49')
###################LIST CREATED OF DEVICES THAT WILL BE PINGED#########################################
device_list = [host2,host3,switch1,switch2,printer1,printer2,printer3,hv,device1,device2,device2b,device3,device4,device5,device6]
#################################PING THE DEVICES/VARIABLES CREATED ABOVE AND OUTPUT RESULTS########## 
for item in device_list:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
	rep = os.system( 'ping ' + item)
	if rep == 0: 
		output=(item+ ' is up: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())) 
	else:
		output=(item+ ' is down: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))	    
	time.sleep(1)
	print ("   ")
	print ("   ")
	print ("   ")
	print (output)

   

