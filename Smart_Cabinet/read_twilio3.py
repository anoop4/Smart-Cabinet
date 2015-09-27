from twilio.rest import TwilioRestClient
account_sid ="ACddc1625ea237d0bda40b17a0a3cb0546"
auth_token = "c8c262efa50088a9160ef86705708ab8"
client = TwilioRestClient(account_sid,auth_token)

from parse_rest.datatypes import Object
from parse_rest.connection import register
register("z6nKgSpt8tWO6rKjKtKj2YR8bXI98akyHpMuTNcD","kZTetWZbEo5lTbSMG0Unoov5nxn4ECjkCDnQKUBa")



with open('smart_cabinet1.txt', 'r') as f:
    data = f.readlines()

    for line in data:
        words = line.split("$")
        #print words

    index=1
    v=""
    c="0"
    for i in words[1::2]:
        if ( int(i) <80 and int(i)!=0):
            v = v +" "+  words[index-1]
	    c = i
        index+=2
    if(v==""):
	print "NO MESSAGE SENT !!"
    else:		
    	 v= v + " needs to be refilled"

   	 message = client.sms.messages.create(body= v,
		to = "+918861007710",
		from_ ="+12512164933")
	 print message.sid


first_object=Object()

class Gateway(Object):
     	 pass
	
#print words
index=0
for i in words[0::2]:
		w=int(words[index+1])
                gateway=Gateway(Container_NO=index+1,Weight=w)
		gateway.save()
		print gateway.objectId
		index+=1

