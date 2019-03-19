"""
A script designed to 1) resize all of the downloaded images to desired dimension (DEFAULT 64x64 pixels) and 2) rename images in folders from 1.png to n.png for ease of use in training
"""

import os
import scipy.misc
import random

root='e:\\art\\data'

size=128

#Set your own PATH 
PATH = os.path.normpath('e:/art/data{}/'.format(size))

for subdir, dirs, files in os.walk(root):
    name =  subdir[subdir.rfind('\\')+1:]
    if len(dirs) > 0:
        continue

    print("Processing category %s" % name)

    try:
        os.stat(os.path.join(PATH,name))
    except:
        os.mkdir(os.path.join(PATH,name))

    
    i = 0
    for f in files:
        source = os.path.join(root,name,f)
        print(str(i) + source)
        try:
            image = scipy.misc.imread(source)
            image = scipy.misc.imresize(image,(size,size))
            scipy.misc.imsave(os.path.join(PATH,name,str(i) + '.png'),image)
            i+=1
        except Exception:
            print('missed it: ' + source)
