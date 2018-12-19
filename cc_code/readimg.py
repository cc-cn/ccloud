import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
import numpy as np

lena = mpimg.imread('/home/deepglint/Documents/data/gun/JPEGImages/000000.jpg') 

print(type(lena))
print(lena.shape)

'''
plt.imshow(lena)
plt.axis('off')
plt.show()
'''
