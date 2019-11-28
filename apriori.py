import collections
from idlelib.multicall import r
import numpy as np
import pandas as pd
from collections import Counter
import itertools
from itertools import chain
from itertools import permutations
from tkinter import *
from itertools import *
import imaplib

# The part responsible for the GUI

'''
root = Tk()
label1 = Label(root, text="Read %", fg="green")
entry1 = Entry(root)
label2 = Label(root, text="Min support", fg="green")
entry2 = Entry(root)
label3 = Label(root, text="Min confidence", fg="green")
entry3 = Entry(root)
label1.grid(row=0, sticky=E)
entry1.grid(row=0, column=1)
label2.grid(row=1, sticky=E)
entry2.grid(row=1, column=1)
label3.grid(row=2, sticky=E)
entry3.grid(row=2, column=1)
button1 = Button(root, text="Submit")
button1.grid(columnspan=2)
root.mainloop()
'''

# The implementation
file = open("CarSales.txt", "r")
num_lines = sum(1 for line in open('CarSales.txt'))

# User chooses how many lines/records he wants to read from the file in percentage.

percentage = int(input("How many % of records you want to read?"))
minSupport = int(input("What is the minimum support?"))
minConfidence = int(input("What is the % of the minimum confidence"))


# Convert the percentage to number of records.
records = int((percentage / 100) * num_lines)

# Variable to store the x% of records/transactions the user wants to read.
dataSet = pd.read_csv("CarSales.txt", sep=' ', header=None, nrows=records).values

# A dictionary that basically shows us how much certain item is repeated.
D = dict()
for quad in dataSet:
    combinations = []
    for i in range(1, 5):
        for a in itertools.combinations(quad, i):
            combinations.append(a)
            # print(D)
    for comb in combinations:
        if comb in D:
            D[comb] = D[comb] + 1
        else:
            D[comb] = 1

copyOfDict = dict(D)
for (key, value) in copyOfDict.items():
    if value < minSupport:
        del D[key]
print("Dic after", D)


maxSize = max(len(x) for x in D)

confidenceKeys = (lambda k: [l for l in D if len(l) == k])(len(max(D, key=len)))
confidenceValues = [D[i] for i in confidenceKeys]
confidenceSubset = []
for x in range(0, len(confidenceKeys)):
    for y in range(0, len(confidenceKeys[0])):
        if confidenceKeys[x][y] in confidenceSubset:
            continue
        else:
            confidenceSubset.append(confidenceKeys[x][y])
combs = []
for quad in confidenceKeys:
    for i in range(1, 3):
        for a in itertools.combinations(quad, i):
            combs.append(a)

confidencePerm = list(permutations(confidenceSubset, maxSize))
test = []

for i in list(confidenceSubset):
    list_num = [i]
    for j in list(confidenceSubset):
        if i == j:
            continue
        else:
            list_num.append(j)
    test.append(list_num)
    test.append(list_num[::-1])
