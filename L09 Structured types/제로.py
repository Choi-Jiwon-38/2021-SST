temp1 = []
temp2 = []

n = int(input())
for i in range(n):
    a = int(input())
    temp1.append(a)
    
    if temp1[i] == 0:
        del temp2[len(temp2)-1]
    else:
        temp2.append(temp1[i])

print(sum(temp2))