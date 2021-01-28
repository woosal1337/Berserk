import cv2
import numpy as np
from pyzbar.pyzbar import decode


def qrDec(imgpath):
    decodedList = []
    img = cv2.imread(imgpath)

    for barcode in decode(img):
        data = barcode.data.decode("utf-8")
    decodedList.append(data)


    print(decodedList)
    return decodedList
