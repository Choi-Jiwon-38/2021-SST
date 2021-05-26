n = int(input())

for i in range(n):
    temp = list(input())
    bracket = 0

    for j in temp:
        if j == '(':
            bracket += 1
        elif j == ')':
            bracket -= 1
        
        if bracket == -1:
            print('NO')
            break
    if bracket > 0:
        print('NO')
    elif bracket == 0:
        print('YES')