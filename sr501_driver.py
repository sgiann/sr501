#code from modmypy.com/blog
import RPi.GPIO as GPIO
import time

#set out pin numbering (?)
GPIO.setmode(GPIO.BCM)

#name our input pin
PIR_PIN = 21

#define pin as input
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print "PIR Module Test (CTRL+C to exit)"
    print "Warm up 60secs. Be patient"
    time.sleep(60)
    print"Ready"

    #check input status of PIR_PIN in an infinite loop
    while True:
        if GPIO.input(PIR_PIN):
            print "Motion Detected!"
        else:
            print "fail"

        time.sleep(1)
except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()
