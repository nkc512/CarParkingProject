import RPi.GPIO as GPIO
from subprocess import call
import time
import os
import glob
import smtplib
import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import subprocess

gmail_user = "dfgsfgs@gmail.com"
gmail_pwd = "********"
FROM = 'dfgsfgs@gmail.com'
TO = ['qwerty@gmail.com'] #must be a list


def send_an_email(location):
    i=1
    while (i):
	i=i-1
	#subprocess.Popen( "fswebcam -r 1280x720 /home/pi/Downloads/pan.jpg", shell=True )
        msg = MIMEMultipart()
	time.sleep(0.1)
        msg['Subject'] ="RaspCamPic"
        fp = open(location, 'rb')
        img = MIMEImage(fp.read())
       	time.sleep(0.1)
        fp.close()
        msg.attach(img)
        try:
                
                server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
                
		print "smtp.gmail"
                server.ehlo()
                
		print "ehlo"
                server.starttls()
                
		print "starttls"
		server.login(gmail_user, gmail_pwd)
		
		print "reading mail & password"		
                server.sendmail(FROM, TO, msg.as_string())
               
		print "from"
                server.close()
                print 'successfully sent the mail'
                return 1
	except:
        	print "failed to send mail"
        	return 0