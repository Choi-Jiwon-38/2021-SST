condition = 1
while (condition):
    line = input()
    a = line.split()
    if int(a[0]) == 0 and int(a[1]) == 0:
        condition = 0
    else:
        print(int(a[0]) + int(a[1]))