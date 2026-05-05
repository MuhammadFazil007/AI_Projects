import cv2
import matplotlib.pyplot as plt
import numpy as np

def histogram(image, channel):
    hist = cv2.calcHist(
        [image],
        [channel],
        mask = None,
        histSize = [256],
        ranges = [0,256]
    )
    plt.bar(range(256),hist.ravel(),width = 1) 
    plt.xlim(0,255)
    plt.ylim(0,3000)
    return plt.gca()    
