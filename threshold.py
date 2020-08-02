import cv2
import numpy as np
import matplotlib.pyplot as plt


def nothing(x):
  pass

cv2.namedWindow('Colorbars')

hh='Max'
hl='Min'
wnd = 'Colorbars'

cv2.createTrackbar("Max", "Colorbars",0,255,nothing)
cv2.createTrackbar("Min", "Colorbars",0,255,nothing)

img = cv2.imread('./dataset/img12.jpg')
scale_percent = 10
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100) 
dim = (width, height) 


img = cv2.resize(img, dim, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]# for i in xrange(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])# plt.show()
while(1):
	hul=cv2.getTrackbarPos("Max", "Colorbars")
	huh=cv2.getTrackbarPos("Min", "Colorbars")
	ret,thresh1 = cv2.threshold(img,hul,huh,cv2.THRESH_BINARY)
	ret,thresh2 = cv2.threshold(img,hul,huh,cv2.THRESH_BINARY_INV)
	ret,thresh3 = cv2.threshold(img,hul,huh,cv2.THRESH_TRUNC)
	ret,thresh4 = cv2.threshold(img,hul,huh,cv2.THRESH_TOZERO)
	ret,thresh5 = cv2.threshold(img,hul,huh,cv2.THRESH_TOZERO_INV)
	   # cv2.imshow(wnd)
	cv2.imshow("thresh1",thresh1)
	cv2.imshow("thresh2",thresh2)
	cv2.imshow("thresh3",thresh3)
	cv2.imshow("thresh4",thresh4)
	cv2.imshow("thresh5",thresh5)
	k = cv2.waitKey(1) & 0xFF
	if k == ord('m'):
	    mode = not mode
	elif k == 27:
	    break

cv2.destroyAllWindows()
