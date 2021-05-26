n = int(input())
num_han = 0
num_list = list(str(n))

if n < 100:
    num_han = n
else:
    num_han = 99
    for i in range(100, n+1):
        a = list(str(i))
        if int(a[0]) - int(a[1]) == int(a[1]) - int(a[2]):
            num_han += 1

print(num_han)
