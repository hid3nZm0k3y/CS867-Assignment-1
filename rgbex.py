def rgbExclusion(filename,rgblist):

#!/usr/bin/env python3
    import cv2
    from PIL import Image
    import numpy
    import sys
    
    im = Image.open(filename).convert("RGB")
    Rmult, Gmult, Bmult = 1, 1, 1

    Rmult = rgblist[0]
    Gmult = rgblist[1]
    Bmult = rgblist[2]

# Select one (or more) channels to zero out
    Matrix = ( Rmult, 0, 0, 0,
           0, Gmult, 0, 0,
           0, 0, Bmult, 0)

    im = im.convert("RGB", Matrix)
    im.save('result.jpg')

