N = int(input())
temp = []

for x in range(0, 1688):
    for y in range(0, 1001):
        if 3 * x + 5 * y == N:
            temp.append(x + y)
            break
        if 5 * y > N:
            break
    if 3 * x > N:
        break

if temp != []:
    print(min(temp))

else:
    print(-1)