import cv2
import glob

class ReadVideoToImage:

  def ReadImg(self,path):
  
     path = "path/audio-video/**/"

#Read images from video using opencv
vidcap = cv2.VideoCapture(path)
success, image = vidcap.read()
count = 1
while success:
  cv2.imwrite("*.*/image_%d.png" % count, image)    
  success, image = vidcap.read()
  print('Saved image ', count)
  count += 1 
  
  
 
 images = cv2.imread("path\*.*")
 
    return images
	
	
 