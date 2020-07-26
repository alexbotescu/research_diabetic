import csv
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
glics=[0 for i in range(1000)]
with open('pacients.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    rcount = 0
    for row in csv_reader:
        rcount=0
        for cols in row:
            rcount+=1
            if(rcount==10 and line_count):
                glics[int(cols)]+=1
        line_count+=1
knt=0
y=[]
xxx=[]
for i in range (0,len(glics)):
    if glics[i]:
        knt+=1
        xxx.append(i)
        y.append(glics[i])
x = np.arange(knt)
fig, ax = plt.subplots()
plt.bar(x, y)
plt.title("Statistica nivel glicemie - nr pacienti")
plt.xticks(x, xxx)
plt.show()