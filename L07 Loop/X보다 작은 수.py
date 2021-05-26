line = input()
a = line.split()

N = int(a[0])
X = int(a[1])

line_2 = input()
b = line_2.split()

temp = []

for i in range(len(b)):
    if int(b[i]) < X:
        temp.append(b[i])

for i in range(len(temp)):
    print(temp[i], end = ' ')