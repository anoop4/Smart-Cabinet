
#import cloud as cl
#import data_packaging as dp
import os
import time

def main():
    #cc=cl.cloud_stuff()
    #dp_run=dp.data()
    while True:
	print "Executing the main program"
	print 'Reading From Sensor'
        os.system("./a.out")
        #tt=time.gmtime()
        #time_stamp=str(tt[2])+':'+str(tt[1])+':'+str(tt[0])+'-'+str(tt[3])+':'+str(tt[4])+':'+str(tt[5])
        #print 'Format data'
	#data,count=dp_run.get_data()
	#print 'Pushing the Data'
        #cc.push_data_parse(data,5)
        #cc.push_data_parse(count,7)
	#print 'Display cloud data'
        #cc.push_data_parse(time_stamp,6)
        #print 'cloud:',cc.status_check_parse(5)
        #print 'cloud:',cc.status_check_parse(7)
        print 'Pushing into Cloud'
        os.system("python read_twilio2.py")
        time.sleep(120)

    # run the c program and write the values to the file
    # run the python code that reads the value from the file
    # repeat
if __name__ == '__main__':
    main()
