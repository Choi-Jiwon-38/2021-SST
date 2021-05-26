line = input()
a = line.split()

N = int(a[0])
K = int(a[1])

temp = []

for i in range(1, K+1):
    num = str(N * i)
    num_r = int(num[::-1])
    temp.append(num_r)

print(max(temp))