n=int(input())

for i in range(n):
    line = input()
    a = line.split()
    sum_all = int(a[0]) + int(a[1])
    print(f'Case #{i + 1}: {a[0]} + {a[1]} = {sum_all}')