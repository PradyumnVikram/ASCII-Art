__author__ = "Pradyumn Vikram"
import cv2
import os

#defining some variables
root = os.path.dirname(__file__)

#loading the image
img = cv2.imread(os.path.join(root, '<IMAGE_NAME (works best with JPEG files)>'), 3)
#resize it if you want using the below line
#img = cv2.resize(img, (120, 200))
rows, cols, pixel = img.shape
array = []

#defining all the ASCII characters to be used in making the art!
to_map = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
#iterating through each pixel
for i in range(rows):
    array.append([])
    for j in range(cols):
        rgb_array = img[i, j]
        #taking average of all RGB values of eavh pixel brighter ones are closer to 255
        avg = (int(rgb_array[0]) + int(rgb_array[1]) + int(rgb_array[2]))/3
        #scaling the avergae image to a value within the ASCII chars length to replace
        if round(round(avg)*65/255) - 1 > 0:
            #replacing the RGB pixel value with the character obtained from its scaled average
            array[i].append(to_map[round(round(avg)*65/255) - 1]*3)
        else:
            array[i].append(to_map[round(round(avg)*65/255)]*3)

#saving the art in a text file
f = open('out.txt', 'w')
for row in array:
    f.write('\n')
    for char in row:
        f.write(char)

f.close()
