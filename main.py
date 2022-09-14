import os

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns; sns.set()
from barcode_generator import*


def hamming_distance(str1, str2):
    d = 0
    for c1, c2 in zip(str1, str2):  # zip() Iterate over several iterables in parallel
        if c1 != c2:
            d = d + 1
    return d

def sum_of_abs_difference(str1, str2):
    d = 0
    for c1, c2 in zip(str1, str2):  # zip() Iterate over several iterables in parallel
        d = d + abs(int(c1)-int(c2))
    return d


cwd = os.getcwd()
print(cwd)
MNIST_path = os.path.join(cwd, 'MNIST_DS')
print(MNIST_path)
classes = os.listdir(MNIST_path)
print(classes)
all_barcodes = {}
for c in classes:
    images_path = os.path.join(MNIST_path, c)
    image_files = os.listdir(images_path)
    for i in image_files:
        path = os.path.join(images_path, i)
        image = Image.open(path)
        arr = np.asarray(image)
        x = barcode_generator(arr)
        key = c+"/"+i
        all_barcodes[key] = x
#print(all_barcodes)

#Test Data for Single Image
"""
c = '0'
image_name = 'img_10007.jpg'
image_path = os.path.join(os.getcwd(), 'MNIST_DS/'+c, image_name)
print("Look For: " + image_path)
image = Image.open(image_path)
array = np.asarray(image)
test = barcode_generator(array)
ham = 162;
for i in all_barcodes.keys():
    calcham = hamming_distance(test, all_barcodes[i])
    if calcham < ham:
        ham = calcham
        result = os.path.join(os.getcwd(), 'MNIST_DS', i)
print("Found: " + result)
im = Image.open(result)
im.show()
"""


def checkall(all_barcodes):
    hits = 0
    for y in all_barcodes.keys():
        #ham = 162;
        test_all_barcodes = all_barcodes.copy()
        test_all_barcodes.pop(y)
        checkClass = y[0]
        image_path = os.path.join(os.getcwd(), 'MNIST_DS', y)
        img = Image.open(image_path)
        array = np.asarray(img)
        test = barcode_generator(array)
        #Search Part
        value = list(test_all_barcodes.values())
        ham = sum_of_abs_difference(test, value[0])
        for j in test_all_barcodes.keys():
            #calcham = hamming_distance(test, test_all_barcodes[j])
            calcham = sum_of_abs_difference(test, test_all_barcodes[j])
            if calcham < ham:
                ham = calcham
                foundClass = j[0]
        #End of Searching
        if foundClass == checkClass:
            hits = hits + 1
    print("The Hit Rate for this algorithm is {}%".format(hits))
    return hits



def checkimage(path, all_barcodes):
    # ham = 162;
    test_all_barcodes = all_barcodes.copy()
    test_all_barcodes.pop(path)
    checkClass = path[0]
    image_path = os.path.join(os.getcwd(), 'MNIST_DS', path)
    img = Image.open(image_path)
    array = np.asarray(img)
    test = barcode_generator(array)
    # Search Part
    value = list(test_all_barcodes.values())
    ham = sum_of_abs_difference(test, value[0])
    for j in test_all_barcodes.keys():
        # calcham = hamming_distance(test, test_all_barcodes[j])
        calcham = sum_of_abs_difference(test, test_all_barcodes[j])
        if calcham < ham:
            ham = calcham
            foundClass = j[0]
            foundpath = j
    # End of Searching
    found_image_path = os.path.join(os.getcwd(), 'MNIST_DS', foundpath)
    found_img = Image.open(found_image_path)
    found_img.show()
    print("The Found Path is {}%".format(found_image_path))

#Test
hitCount = checkall(all_barcodes)
checkimage("8/img_10024.jpg", all_barcodes)




