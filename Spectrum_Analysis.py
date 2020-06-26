import matplotlib
import matplotlib.pyplot as plt
import numpy as np

with open("csvSpectrum.txt", "r") as test:
    rawData = test.readlines()
test.close()
dataProcessed = []
for x in range(1, len(rawData)):
    line = rawData[x].split('\n')
    line.pop(1)
    for data in line:
        finalData = data.split(',')
        dataProcessed.append([float(finalData[0]), float(finalData[2])])
x = []
y = []

for point in dataProcessed:
    x.append(point[0])
    y.append(point[1])
    
plt.plot(x, y)
plt.savefig("plot.png")
