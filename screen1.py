import numpy as np
import cv2
from mss import mss
from PIL import Image

#mon = {'top': 160, 'left': 160, 'width': 200, 'height': 200}
#cords = {'top':40 , 'left': 0 , 'width': 800, 'height': 640 }
def grab_screen():
#sct = mss()
 bbox=(30,103,1365,325) 
  
#    sct.get_pixels(cords)
#    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
 with mss() as sct :
        #img = sct.grab(bbox)
        #img = np.array(sct.grab(bbox))
        img = np.array(sct.grab(bbox),dtype='uint8')
        #img = np.frombuffer(im, dtype='uint8')
        
 return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)     


 
