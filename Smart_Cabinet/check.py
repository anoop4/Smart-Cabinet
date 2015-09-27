import os
import time
from parse_rest.datatypes import Object
from parse_rest.connection import register
register("z6nKgSpt8tWO6rKjKtKj2YR8bXI98akyHpMuTNcD","kZTetWZbEo5lTbSMG0Unoov5nxn4ECjkCDnQKUBa")

first_object=Object()

class Gateway(Object):
     	 pass
         
readings=Gateway.Query.all()
while True:
    print "objectId            Container_NO            Weight"

    for value in readings:
       print("%s               %d                    %d" %(value.objectId,value.Container_NO,value.Weight))
    if(value.Container_NO==0 and value.Weight==0):
      	print" ******** REQUEST RECEIVED FROM THE APP ********** "
        print "Reading Sensor value"
        os.system("./a2")
        print " Pushing into cloud"
        os.system("python read_twilio3.py")
        #smart=Gateway.Query.get(objectId=value.objectId)
        #print smart.objectId
        #smart.delete()
    
