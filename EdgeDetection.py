import cv2
import sys

image = cv2.imread('Images\edgeDetection.jpg')

#converting image into grayscale

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray_image, 30,100)
cv2.imshow("edged", edges)
cv2.waitKey(0)

tresh = cv2.threshold(gray_image, 255, 255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow("trsh",tresh)
cv2.waitKey(0)