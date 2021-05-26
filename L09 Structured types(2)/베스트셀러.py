n = int(input())
temp = []

for _ in range(n):
    a = input()
    temp.append(a)

temp_set = set(temp)
index = {}

for i in temp_set:
    count = temp.count(i)
    index[i] = count
    count = 0

temp_print = []
keys = list(index.keys())
values = list(index.values())

for j in range(len(keys)):
    if values[j] == max(values):
        temp_print.append(keys[j])

temp_print = sorted(temp_print)

print(temp_print[0])