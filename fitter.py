import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys
import csv

filename = 'CurveRecTestWell.CSV'
data = []
with open(filename, "r") as file_to_read:
    reader = csv.reader(file_to_read)
    for line in reader:
        data.append(line)
label = data[0]
data.pop(0)
Length = len(label) - 1
proper = []
for i in range(len(label) - 1):
    can = []
    proper.append(can)
for i in data:
    for j in range(len(label) - 1):
        proper[j].append(float(i[j + 1]))
### 目标拟合函数 Objective fittting function

def residuals(p, Length, data):
    Len1 = len(data[0])
    Sum = []
    for i in range(Len1):
        sum1 = data[Length - 1][i] - p[Length - 1]
        for j in range(Length - 1):
            sum1 = sum1 - data[j][i] * p[j]
        Sum.append(sum1)
    return Sum

### 输出参数 Output parameter

p0 = [1, 1, 0]
#Sum = residuals(p0, Length, proper)
#print(Sum)
r = optimize.leastsq(residuals, p0, args=(Length, proper))
print(r[0])
k1, k2, b = r[0]
print("k1 = ",k1, "k2 =",k2, "b =",b)
print("y = (",k1, ")x1 + (",k2, ")x2 + (",b, ")")