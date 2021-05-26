n = int(input())

for i in range(n):
    print('*'*(1 + i))
    if i == n - 1:
        for i in range(n - 1):
            print('*'*(n - i - 1))