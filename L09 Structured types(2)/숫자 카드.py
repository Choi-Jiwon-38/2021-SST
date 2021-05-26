import sys

n = int(sys.stdin.readline())

temp_1 = list(sys.stdin.readline().split())
temp_1_set = set(temp_1)
index = {}

for i in temp_1_set:
    count = temp_1.count(i)
    index[i] = count

m = int(sys.stdin.readline())
temp_2 = list(sys.stdin.readline().split())
temp_print = []
z = 0

for j in temp_2:
    if temp_2[z] in index: 
        temp_print.append(index[j])
    else:
        temp_print.append(0)
    z += 1

for k in range(len(temp_print)):
    print(temp_print[k], end = ' ')