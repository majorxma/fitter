import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys
import csv

#读入csv数据
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

p0 = []
for i in range(Length - 1):
    p0.append(1)
p0.append(0)

#进行拟合
r = optimize.leastsq(residuals, p0, args=(Length, proper))

#输出结果
result = r[0]

for i in range(len(result) - 1):
    print("k" + str(i + 1) + " = " + str(result[i]))
print("b = " + str(result[len(result) - 1]))

Str = "y = "
for i in range(len(result) - 1):
    Str += ("(" + str(result[i]) + ")x" + str(i + 1) + " + ")
Str += ("(" + str(result[len(result) - 1]) + ")")
print(Str)