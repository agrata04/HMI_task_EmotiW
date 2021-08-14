from ReadVideoToImage import ReadImg
from Read3Dimage import image_to_df
from SVC_run import SVC_method

path = "*.*"

images = ReadImg(path)
df = image_to_df(images)
SVC_classify = SVC_method(df)

