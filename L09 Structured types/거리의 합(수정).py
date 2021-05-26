n = int(input())
x = sorted(map(int, input().split()))

l = list(range(-2*(n-1), 2*(n+1)+1, 4))

s = 0

#for i in range(len(x)):
#    s += x[i] * l[i]

#print(s)

for a, b in zip(x, l):
    s += a * b

print(s)