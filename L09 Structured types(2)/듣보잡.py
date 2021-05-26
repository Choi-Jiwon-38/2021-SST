line = input()
a = line.split()

temp1 = []
temp2 = []
temp3 = []

for i in range(int(a[0])):
    temp1.append(input())

for j in range(int(a[1])):
    temp2.append(input())

for k in range(int(a[0])):
    for j in range(int(a[1])):
        if temp1[k] == temp2[j]:
            temp3.append(temp1[k])

temp3.sort()
print(len(temp3))

for t in range(len(temp3)):
    print(temp3[t])