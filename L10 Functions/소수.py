m = int(input())
n = int(input())
temp = []

for i in range(m, n+1):
    count = 0
    for j in range(1 , i+1):
        if i % j == 0:
            count = count + 1
            if count > 2:
                pass
    if count == 2:
        temp.append(i)

if len(temp) >= 1:
    print(sum(temp))
    print(temp[0])
else:
    print('-1')
