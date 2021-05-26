num_all = []
temp = []
self_num = []

for x in range(1,10001):
    num_all.append(x)

for i in range(1,10001):
    num = list(str(i))
    num = map(int, num)
    d_num = sum(num) + i
    temp.append(d_num)

s = set(temp)
self_num = [y for y in num_all if y not in s]

for _ in self_num:
    print(_)