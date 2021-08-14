# HMI_task_EmotiW

Prequiresits

1.OPencv for reading and writing images 2.Menpofit for Supervised decent method 3.LBP_top algortihm for feature extraction 4.SKlearn for SVC with chi-squared kernel for classification

All the pre-requistis are included in src .see src files for more information

This is the demo code.(see demo.py)


from ReadVideoToImage import ReadImg
from Read3Dimage import image_to_df
from SVC_run import SVC_method

path = "*.*"

images = ReadImg(path)
df = image_to_df(images)
SVC_classify = SVC_method(df)


