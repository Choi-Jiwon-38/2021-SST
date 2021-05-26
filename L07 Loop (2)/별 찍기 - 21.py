n = int(input())

def figure(n):
    for i in range(n):
        if i % 2 == 0:
            print('*', end = '')
        
        if i % 2 == 1:
            print(' ', end = '')

    print()

    for t in range(n):
        if t % 2 == 0:
            print(' ', end = '')
        if t % 2 == 1:
            print('*', end = '')

for z in range(n):
    if z == n - 1:
        figure(n)
        break
    else:
        figure(n)
        print()