#code from modmypy.com/blog
import RPi.GPIO as GPIO
import time
import datetime
import os.path as path

print "Initialize"

#set out pin numbering
GPIO.setmode(GPIO.BCM)
#name and set our input pin
PIR_PIN = 21
#define pin as input
GPIO.setup(PIR_PIN, GPIO.IN)

#check and initialize file
fileName = "/home/pi/Documents/sr501_log.txt"
fileMode = "a"
fileBuffered = 1
##if (path.isfile(filename)):
##    #open file
##    #fileHandler
##    print "Under construction"
##else:
##    #create file
logFileHandler = open(fileName, fileMode, fileBuffered)
logFileHandler.write("Start\n")
try:
    print "PIR Module Test (CTRL+C to exit)"
    time.sleep(2)
    print"Ready"

    #check input status of PIR_PIN in an infinite loop
    while True:
        if GPIO.input(PIR_PIN):
            #set timestamp variable
            ts = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S %d-%m-%Y')
            logFileHandler.write(ts + "\n")
            print "Motion Detected!" + ts
            
        time.sleep(1)
except KeyboardInterrupt:
    logFileHandler.write("End\n\n")
    logFileHandler.close()
    print "Quit"
    GPIO.cleanup()
