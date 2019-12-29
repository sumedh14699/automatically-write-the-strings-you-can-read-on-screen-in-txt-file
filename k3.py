import cv2
import pytesseract
from screen1 import grab_screen
#import Image
f = open("exp.txt", "a")
while True:
      screen = cv2.resize(grab_screen(), (1335,222))
      image_np = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
      f.write(pytesseract.image_to_string(image_np))
      cv2.imshow('window',image_np)

      if cv2.waitKey(25) & 0xFF == ord('q'):
          cv2.destroyAllWindows()
          f.write("\nE\nE\nE\nE\nE\nE\n\n\n\nEND OF PROGRAM\n\n\n\nP\nP\nP\nP\nP\nP\n")
          f.close()
          break

# OR explicit beforehand converting
#print(pytesseract.image_to_string(Image.fromarray(img)))
