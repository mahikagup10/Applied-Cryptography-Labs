import numpy as np
key = "WORK"
pt = "CRYPTOGRAPHY"

ct = ""
array1 = []     #to store the paired chars
array2 = []     #to store the key letters

for i in (range(len(pt))-1):
    char1 = pt[i]
    char2 = pt[i+1]
    array1.append(char1+char2)

matrix = []

for i in range(len(key)):
    array2[i] = key[i]

for i in range(len(array2)):
    matrix.append(array2[i])

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for i in letters:
    if i not in matrix:
        matrix.append(i)




