temp = []

for i in range(10):
    a = int(input())
    b = a % 42
    temp.append(b)

temp = set(temp)

print(len(temp))