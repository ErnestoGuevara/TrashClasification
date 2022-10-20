import cv2
import os
import tensorflow as tf
from tensorflow import keras
import numpy as np
import time

# Recrea exactamente el mismo modelo

new_model = keras.models.load_model('/Users/ernestoguevara/Desktop/Trash_clasification/content/carpeta_salida/modelo_basura/1')
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

    cv2.imshow('video', frame)

    key = cv2.waitKey(1)
    if key%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    if time.time() - start_time >= 5: #<---- Check if 5 sec passed
        img_name = "opencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        start_time = time.time()
        img_counter += 1
        if img_counter == 1:
          break
    
direc = '/Users/ernestoguevara/Desktop/trash_clasification/lata1.jpeg'
cam.release()
cv2.destroyAllWindows()
prediccion = categorize(direc)
if(prediccion == 0):
  print("Metal")
if(prediccion == 1):
  print("Plastic")
if(prediccion == 2):
  print("Glass")
if(prediccion == 3):
  print("Other")
