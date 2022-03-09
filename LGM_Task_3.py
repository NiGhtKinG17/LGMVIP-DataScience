"""This is program for coverting an image to pencil sketch using
OpenCV library of Python"""

#For installing opencv library type the following command in the terminal:
#pip install opencv-python

#We will start by importing the library opencv
import cv2

#Get the image from a file. We have image in the same folder as our program so we need not to give full path
#If your image is in another folder, then you need to give full path for that image
file = 'japan.jpg'

#Read our image
img = cv2.imread(file)

#Show the image
cv2.imshow("Original image",img)

#Now we will convert the image to grayscale using cvt funtion of opencv
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)

#We will invert the image 
inverted_gray = 255 - gray

#In this step we will blur our inverted gray image using gaussianblur function
blurred = cv2.GaussianBlur(inverted_gray, (25,25), 0)

#We will again invert the blurred image
inverted_blur = 255 - blurred

#Finally we will get the sketch by dividing the gray image with inverted blurred image
sketch = cv2.divide(gray, inverted_blur, scale= 256.0)
cv2.imshow("Sketch", sketch)

#We need to give the waitkey so that our image doesn't close until we close it
cv2.waitKey(0)
#At last we need to destroy all the created windows
cv2.destroyAllWindows()

'''Thank You!
    By Hritik Shelar'''