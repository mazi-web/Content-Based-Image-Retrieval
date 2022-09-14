import numpy as np


def average(l):
    return sum(l) / len(l)


def generate_c(p, r_average):
    c = []
    for item in p:
        if item >= r_average:
            c.append(1)
        else:
            c.append(0)
    return c


def barcode_generator(arr):
    #Creates 4 list for the 4 vectors of projection 0, 45, 90, and 135
    zeroD = []
    foufiveD = []
    nineD = []
    onethirfiveD = []

    #Sums all elements across the each row and append them to the zeroD vector list
    for i in range(28):
        zeroD.append(np.sum(arr[i, :]))

    #Sums all elements across the each column and append them to the nineD vector list
    for j in range(28):
        nineD.append(np.sum(arr[:, j]))

    #Sum each diagonal an append them to the 45 degrees vector diagonal
    foufiveD.append(np.sum(np.diagonal(arr, 0, 0, 1)))
    for k in range(1, 53):
        x = np.sum(np.diagonal(arr, -k, 0, 1))
        foufiveD.append(np.sum(np.diagonal(arr, k, 0, 1)))
        #foufiveD = np.insert(foufiveD, 0, x)
        foufiveD.insert(0, x)

    #Rotate the arr so that the diagonal function grabs the desired elements
    rotatedarr = np.rot90(arr)
    #Sum each diagonal an append them to the 45 degrees vector diagonal
    onethirfiveD.append(np.sum(np.diagonal(arr, 0, 0, 1)))
    for m in range(1,53):
        x = np.sum(np.diagonal(arr, m, 0, 1))
        onethirfiveD.append(np.sum(np.diagonal(arr, -m, 0, 1)))
        #onethirfive = np.insert(onethirfive, 0, x)
        onethirfiveD.insert(0, x)

    #Printing all vector list for monitoring purposes
    #print(zeroD)
    #print(nineD)
    #print(len(foufiveD))
    #print(onethirfive)

    #Generating C1, C2, C3 and C4 using the average function and generate_c function
    avgZ = average(zeroD)
    C1 = generate_c(zeroD, avgZ)

    avgN = average(nineD)
    C2 = generate_c(nineD, avgN)

    avgF = average(foufiveD)
    C3 = generate_c(foufiveD, avgF)

    avgO = average(onethirfiveD)
    C4 = generate_c(onethirfiveD, avgO)

    #Turning C1, C2, C3 and C4 to lists
    String_c1 = [str(n) for n in C1]
    String_c2 = [str(n) for n in C2]
    String_c3 = [str(n) for n in C3]
    String_c4 = [str(n) for n in C4]

    String_d1 = [str(n) for n in zeroD]
    String_d2 = [str(n) for n in foufiveD]
    String_d3 = [str(n) for n in nineD]
    String_d4 = [str(n) for n in onethirfiveD]

    #Addind C1, C2, C3 and C4 to 1 main list
    listbarcode = String_c1+String_c3+String_c2+String_c4
    newbarcode = String_d1+String_d2+String_d3+String_d4
    #Converting listbarcode list to a string
    barcode = ''.join(listbarcode)
    #print(barcode)
    #print(len(barcode))
    #return barcode
    return newbarcode

