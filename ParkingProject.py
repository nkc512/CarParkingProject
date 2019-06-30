# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD
GPIO.setwarnings(False) 
#import email
#from RPLCD import CharLCD
from picamera import PiCamera
from EmailFile import send_an_email
sensor1 = 16
sensor2 = 18
camera = PiCamera()


GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor1,GPIO.IN)
GPIO.setup(sensor2,GPIO.IN)
print ('IR Sensor Ready')
disp=0
i=0
max=5
lcd = CharLCD(numbering_mode=GPIO.BOARD,cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
lcd.write_string('-----Welcome----')
lcd.write_string('Places vacant: 5')
try:
    while True:
        if not GPIO.input(sensor1) and disp<max:
            count=0
            while count<50:
                if not GPIO.input(sensor1) and not GPIO.input(sensor2):
                    count1=0
                    while count1<50:
                        if GPIO.input(sensor1) and not GPIO.input(sensor2):
                            disp=disp+1
                            
                            #lcd.write_string('Places vacant:',max-disp)
                            camera.start_preview()
                            time.sleep(3)
                            location='/home/pi/Desktop/image%s.jpg' % i
                            camera.capture(location)
                            camera.stop_preview()
                            #message.attach(MIMEText(body, "plain"))
                            filename = location
                            lcd.write_string('-----Welcome----')
                            lcd.write_string('--Sending Mail--')
                            response=send_an_email(location)
                            if response == 1:
                                lcd.write_string('-----Welcome----')
                                lcd.write_string('---Email Sent---')
                            else:
                                lcd.write_string('-----Welcome----')
                                lcd.write_string('--Email Not Sent-')
                            time.sleep(0.5)
                            print('Email Sent')
                            if disp<max:
                                print('Places vacant:',max-disp)
                                lcd.write_string('-----Welcome----')
                                lcd.write_string('Places vacant: %s' % (max-disp))
                            else:
                                print('No places vacant')
                                lcd.write_string('-----Welcome----')
                                lcd.write_string('---No vacancy---')
                            i=i+1 
                            count=51
                            break
                        count1=count1+1
                        time.sleep(0.1)
                count=count+1
                time.sleep(0.1)
            print ('working 1')
        if not GPIO.input(sensor2):
            print ('working 2')
            count=0
            while count<50:
                if not GPIO.input(sensor1) and not GPIO.input(sensor2):
                    count1=0
                    while count1<50:
                        if GPIO.input(sensor2) and not GPIO.input(sensor1):
                            if disp >0:
                                disp=disp-1
                            print('Places vacant:',max-disp)
                            lcd.write_string('-----Welcome----')
                            lcd.write_string('Places vacant: %s' % (max-disp))
                            #lcd.write_string('Places vacant:',max-disp)                            
                            count=51
                            break
                        count1=count1+1
                        time.sleep(0.1)
                count=count+1
                time.sleep(0.1)
            print ('working 2')
            
except KeyboardInterrupt:
    lcd.clear()
    camera.stop()
    GPIO.cleanup()
    
    

