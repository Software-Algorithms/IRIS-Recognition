import numpy as np
import pywt
import cv2    

def w2d(img, mode='haar', level=1):
    imArray = cv2.imread(img,0)
    #Datatype conversions
    #convert to grayscale
    print(imArray)
    imArray = cv2.cvtColor( imArray,cv2.COLOR_GRAY2BGR )
    #convert to float
    imArray =  np.float32(imArray)   
    imArray /= 255;
    # compute coefficients 
    coeffs=pywt.wavedec2(imArray, mode, level=level)

    #Process Coefficients
    coeffs_H=list(coeffs)  
    coeffs_H[0] *= 0;  

    # reconstruction
    imArray_H=pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255;
    imArray_H =  np.uint8(imArray_H)
    #Display result
    cv2.imshow('image',imArray_H)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

w2d('m.jpg','db1',1)
