import RPi.GPIO as GPIO
import time
import os
import glob
#GPIO SETUP
GPIO.setmode(GPIO.BCM)
Button = 7
n = 1
GPIO.setup(Button,GPIO.IN)
#loop
print("Program Running")
while 1 == 1:#Devre surekli calisacak 
  if GPIO.input(Button) == False:#Buttona basildi
    print("Button Pressed")
    
    #    ------|    photo & Bell    |------ #
    #Belge isimlendirme
    now = time.strftime("Date%m-%d-%yTime%H-%M-%S")
    #Main.sh calıstırmak icin
    command = "bash main.sh " +  str(now)
    
    # -- Main.sh bir Shell script dosyası
    # -- Fotograf cekiminden sorumlu
    # -- -----------------
    
    
    
    #run command
    os.system(command)
    #diagnostics
    print("Filename:", now)
    
  
    # ----| Email     |---- #
    print("Email")#email
    emailcommand = 'python3 MailNotify.py "Someone is at the door"' + ' "foto/' + now + '.jpg"'
    os.system(emailcommand) #Email scripti calisiyor
    # -- End Diagnostic Info
    print("Done Process")
    #Bosluk
    print("")
    print("")
