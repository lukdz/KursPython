import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

def keep(numbers):
    return [max(0,min(i,1)) for i in numbers]

def happy(img):
    me = np.mean(img, axis=2)
    su = np.sum(np.absolute(img-me[:, :, np.newaxis]), axis=2)
    for i in range(1, img.shape[0]):  
        for j in range(img.shape[1]):
            m = me[i, j]
            if su[i, j] < 0.45*m:
                img[i, j] = keep(m+(3*(img[i, j]-m)))
def sad(img):
    me = np.mean(img, axis=2)
    su = np.sum(np.absolute(img-me[:, :, np.newaxis]), axis=2)
    for i in range(1, img.shape[0]):  
        for j in range(img.shape[1]):
            m = me[i, j]
            if su[i, j] > 0.7*m:
                img[i, j] = keep(m+(0.1*(img[i, j]-m)))

img = []
img.append(mpimg.imread('./ii1.png'))
img.append(img[0].copy()) 
img.append(img[0].copy()) 
sad(img[0])
happy(img[2])

f, axarr = plt.subplots(1,3)
for i in range(3):
    axarr[i].imshow(img[i])
plt.show()
