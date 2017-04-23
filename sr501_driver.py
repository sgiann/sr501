#code from modmypy.com/blog
import RPi.GPIO as GPIO
import time
import datetime

#set out pin numbering
GPIO.setmode(GPIO.BCM)

#name our input pin
PIR_PIN = 21

#define pin as input
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print "PIR Module Test (CTRL+C to exit)"
    time.sleep(2)
    print"Ready"

    #check input status of PIR_PIN in an infinite loop
    while True:
        if GPIO.input(PIR_PIN):
            #set timestamp variable
            ts = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S %d-%m-%Y')
            print "Motion Detected!" + ts
        #else:
        #    print "fail"

        time.sleep(1)
except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()
