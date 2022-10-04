import cv2
import os
from imutils import paths

# Read an image:
def readImage(imagePath):
    # Loads image:
    inputImage = cv2.imread(imagePath)
    # Checks if image was successfully loaded:
    if inputImage is None:
        print("readImage>> Error: Could not load Input image.")

    return inputImage

# Defines a re-sizable image window:
def showImage(imageName, inputImage, delay=0):
    cv2.namedWindow(imageName, flags=cv2.WINDOW_GUI_NORMAL)
    cv2.imshow(imageName, inputImage)
    cv2.waitKey(delay)

# Writes an PNG image:
def writeImage(imagePath, inputImage):
    imagePath = imagePath + ".png"
    cv2.imwrite(imagePath, inputImage, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    print("Wrote Image: " + imagePath)

pathImgTransform = "/Users/ernestoguevara/Desktop/Trash_clasification/imgTransform/"
pathDataSet = "/Users/ernestoguevara/Desktop/Trash_clasification/data/Garbage_classification/"
transformFiles = os.listdir(pathImgTransform)
counterMetal=0
counterPlastic=0
counterGlass=0
for i in transformFiles:
        imagePaths = os.listdir(pathImgTransform + i)
        #print(imagePaths)
        for imagePath in imagePaths:
            
            # Read the image:
            
            inputImage = cv2.imread(pathImgTransform+i+"/"+imagePath)
            #showImage(imagePath, inputImage)
            newWidth = 512
            newHeight = 384
            #set new size
            newSize = (newWidth,newHeight)
            outputImage = cv2.resize(inputImage,newSize,cv2.INTER_AREA)
            #showImage("Resized: "+imagePath, outputImage)
            if (i=="metal"):
                counterMetal+=1
                newImagePath= pathDataSet + "metal/"+ "metal"+str(counterMetal)+".jpg" 
                print("Writting on: "+newImagePath)
                cv2.imwrite(newImagePath, outputImage)
            if (i=="plastic"):
                counterPlastic+=1
                newImagePath= pathDataSet + "plastic/"+ "plastic"+str(counterPlastic)+".jpg" 
                print("Writting on: "+newImagePath)
                cv2.imwrite(newImagePath, outputImage)
            if (i=="glass"):
                counterGlass+=1
                newImagePath= pathDataSet + "glass/"+ "glass"+str(counterGlass)+".jpg" 
                print("Writting on: "+newImagePath)
                cv2.imwrite(newImagePath, outputImage)
            





