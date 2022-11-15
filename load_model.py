import cv2
import os
import tensorflow as tf
from tensorflow import keras
import numpy as np
import time
from time import sleep
import RPi.GPIO as GPIO

servoMiddlePIN = 4
servoGripper = 27
servoTapa = 22
sensor = 5


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Setup of Servo Outputs and sensor input
GPIO.setup(servoGripper,GPIO.OUT)
GPIO.setup(servoMiddlePIN, GPIO.OUT)
GPIO.setup(servoTapa, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)
pwmMiddle = GPIO.PWM(servoMiddlePIN, 50)
pwmGripper = GPIO.PWM(servoGripper, 50)
pwmTapa = GPIO.PWM(servoTapa,50)

pwmMiddle.start(0)
pwmGripper.start(0)
pwmTapa.start(0)
def SetAngleMiddle(angle):
	duty = angle / 18 + 2
	GPIO.output(servoMiddlePIN, True)
	pwmMiddle.ChangeDutyCycle(duty)
	sleep(0.5)
	GPIO.output(servoMiddlePIN, False)
	pwmMiddle.ChangeDutyCycle(0)
def SetAngleGripper(angle):
    duty = angle / 18 + 2
    GPIO.output(servoGripper,True)
    pwmGripper.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoGripper, False)
    pwmGripper.ChangeDutyCycle(0)
def SetAngleTapa(angle):
    duty = angle / 18 + 2
    GPIO.output(servoTapa,True)
    pwmTapa.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoTapa,False)
    pwmTapa.ChangeDutyCycle(0)

SetAngleMiddle(0)

while True: 
    if GPIO.input(sensor):
        print("Nothing detected")
        while GPIO.input(sensor):
            time.sleep(0.2)
    else:
        print("Detected")
        SetAngleMiddle(150)
        #pwmGripper.stop()
        
            
# Recrea exactamente el mismo modelo
new_model = keras.models.load_model('/home/robotics/Desktop/TrashClasification/content/carpeta_salida/modelo_basura/1')
# Verifique que el estado esté guardado

def categorize(dir):
  img = cv2.imread(dir)
  img = np.array(img).astype(float)/255
  img = cv2.resize(img, (224,224))

  try:
    prediccion = new_model.predict(img.reshape(-1, 224, 224, 3))
    print(prediccion)
    #Second index more high
    #print(np.argsort(np.max(prediccion, axis=0))[-2])
    maximum = np.max(prediccion)*100
    print(maximum)
    #if(maximum<88):
      #return 3
    #else:
    return np.argmax(prediccion[0], axis=-1)
   
    
  except ValueError:
    print("Error")

#direc = '/Users/ernestoguevara/Desktop/MODELOBASURA/exapmle8.jpg'
#Start the camera!
start_time = time.time()
img_counter = 0
cam = cv2.VideoCapture(0) 

while True:
    check, frame = cam.read()

    #cv2.imshow('video', frame)

    key = cv2.waitKey(1)
    if key%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    if time.time() - start_time >= 0.5: #<---- Check if 5 sec passed
        img_name = "opencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        start_time = time.time()
        img_counter += 1
        if img_counter == 1:
          break

direc = '/home/robotics/Desktop/TrashClasification/opencv_frame_0.jpg'
cam.release()
cv2.destroyAllWindows()
prediccion = categorize(direc)
if(prediccion == 0):
  print("Metal")
  SetAngleMiddle(50) 


if(prediccion == 1):
  print("Plastic")
  SetAngleMiddle(150) 
  #Add time to set angle in 0
 
  

if(prediccion == 2):
  print("Glass")
  SetAngleMiddle(0) 
  
if(prediccion == 3):
  print("Other")

time.sleep(5)
SetAngleMiddle(0)
#print("hola")
pwmMiddle.stop()
GPIO.cleanup()
