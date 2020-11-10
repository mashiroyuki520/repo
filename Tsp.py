import random
import math
from random import sample
from math import sqrt

n = input("print city number")
sample_size =130
index_x_list = random.sample(range(1,sample_size),n)
index_y_lsit = random.sample(range(1,sample_size),n)
node_list=[]

for index in range(n):
     node_list.append([index_x_list[index],index_y_lsit[index]])

#计算距离
dist_list=list()
for i in range(n):
    row_list = []
    for j in range(n):
        one_dist = math.sqrt(
            pow((node_list[i][0]-node_list[j][0]),2)
            pow((node_list[i][1]-node_list[j][1]),2)
             )
        row_list.append(one_dist)
    dist_list.append(row_list)

#产生随机断点
for i in range(random.randint(0,n)):
    x_y = random.sample(range(0,n),2)
    if x_y[0] != x_y[1]:
        dist_list[x_y[0]][x_y[1]] = 0xfffffffff
        dist_list[x_y[1]][x_y[0]] = 0xfffffffff

#tangxingsuanfa
odr = list()
odr[0] = 0
m = 0
tempd =0xfffffff
p = 1
Sum = 0
for ntcy in range(1,n):
    for p in range(1,n):
        if p not in odr and dist_list[ntcy-1][p] <= tempd :
            tempd = dist_list[ntcy-1][p]
            m = p
    if m == 0 :
        print("no solution!")
    odr.append(m)
    Sum += tempd
Sum += dist_list[0][ord[n-1]]

print(odr)
print(Sum)







        




