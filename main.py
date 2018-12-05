from PIL import Image
import scipy.misc
from scipy.misc import toimage, imsave
import math
import numpy
import numpy as np

#initialize the height and width of image
we = 96  #665
he = 160  #443

#initialize global numpy arrays used in the Canny Edge Detector
newgradientgx = np.zeros((he, we))
newgradientgy = np.zeros((he, we))
newgradientImage = np.zeros((he, we))
tan = np.zeros((he, we))


#function to perform Prewitt operator
def prewitt(b):
    gray_img = b
    print("The values of the read image are ")
    print(gray_img)

    # Prewitt Operator
    h, w = gray_img.shape
    # define filters
    horizontal = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    vertical = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

    #offset each edge by 1
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            horizontalGrad = (horizontal[0, 0] * gray_img[i - 1, j - 1]) + \
                             (horizontal[0, 1] * gray_img[i - 1, j]) + \
                             (horizontal[0, 2] * gray_img[i - 1, j + 1]) + \
                             (horizontal[1, 0] * gray_img[i, j - 1]) + \
                             (horizontal[1, 1] * gray_img[i, j]) + \
                             (horizontal[1, 2] * gray_img[i, j + 1]) + \
                             (horizontal[2, 0] * gray_img[i + 1, j - 1]) + \
                             (horizontal[2, 1] * gray_img[i + 1, j]) + \
                             (horizontal[2, 2] * gray_img[i + 1, j + 1])

            verticalGrad = (vertical[0, 0] * gray_img[i - 1, j - 1]) + \
                           (vertical[0, 1] * gray_img[i - 1, j]) + \
                           (vertical[0, 2] * gray_img[i - 1, j + 1]) + \
                           (vertical[1, 0] * gray_img[i, j - 1]) + \
                           (vertical[1, 1] * gray_img[i, j]) + \
                           (vertical[1, 2] * gray_img[i, j + 1]) + \
                           (vertical[2, 0] * gray_img[i + 1, j - 1]) + \
                           (vertical[2, 1] * gray_img[i + 1, j]) + \
                           (vertical[2, 2] * gray_img[i + 1, j + 1])

            newgradientgx[i, j] = round(horizontalGrad)
            newgradientgy[i, j] = round(verticalGrad)

            if(newgradientgx[i,j]==0):
                tan[i,j]=90.00
            elif (newgradientgx[i, j] == 0 and newgradientgy[i, j] == 0):
                tan[i, j] = 0.00
            else:
                tan[i,j]=math.degrees(math.atan(newgradientgy[i,j]/newgradientgx[i,j]))
                if (tan[i,j]<0):
                    tan[i,j]= tan[i,j] + 360

            mag = np.sqrt(pow(horizontalGrad, 2.0) + pow(verticalGrad, 2.0))
            newgradientImage[i, j] = mag


#function to extrcat HOG features
def hog(b):
    #gray_image = b
    #window_size = 128 x 64
    #cell size = 8 x 8
    #block size = 16 x 16 # or 2 x 2 cells),
    #block overlap step size = 8 pixels #(or 1 cell).
    print("ok")

#Driver Program
indimage = scipy.misc.imread("test_color.bmp")
print(indimage.shape)

#Split the numpy array into RGB channels
red=indimage[:,:,0]
green=indimage[:,:,1]
blue=indimage[:,:,2]

grey = (0.299 * red) + (0.587 * green) + (0.114 * blue)

scipy.misc.imsave('working_files/test_grey.bmp', grey)


prewitt(grey)
scipy.misc.imsave('working_files/test_x_gradient.bmp', newgradientgx)
scipy.misc.imsave('working_files/test_y_gradient.bmp', newgradientgy)
scipy.misc.imsave('working_files/test_magnitude.bmp', newgradientImage)

print(newgradientImage)
numpy.savetxt('working_files/gradient_x.txt',newgradientImage, delimiter=',', fmt='%i')
numpy.savetxt('working_files/arctan.txt',tan, delimiter=',', fmt='%i')

print(np.min(tan))

print(np.max(tan))

#hog(newgradientImage)


#toimage(grey).show()
#toimage(newgradientgx).show()
#toimage(newgradientgy).show()
#toimage(newgradientImage).show()

#numpy.savetxt('rgb_raw_values.txt',indimage, delimiter=',', fmt='%i')

#print(indimage)
#toimage(newgradientgx).show()
#numpy.savetxt('gradient255.txt',newgradientImage, delimiter=',', fmt='%i')
#
#imsave('xgradient.bmp', newgradientgx)
#imsave('ygradient.bmp', newgradientgy)
#imsave('magnitude.bmp', newgradientImage)
