temp = []

n = int(input())

for i in range(n):
    a = int(input())
    temp.append(a)

temp = sorted(temp)

for j in range(n):
    print(temp[j])