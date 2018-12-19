import os
import Image
fileName = '/home/chencheng/data/yingshi_include_xml/0001024.jpg'
fp = open(fileName,'rb')
im = Image.open(fp)
fp.close()
x,y = im.size

print(x,y)
