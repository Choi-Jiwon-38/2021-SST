import sys

n = int(input())
temp = list(map(int, sys.stdin.readline().split()))

distance = 0

for i in temp:
    for j in temp:
        distance += abs(i-j)

print(distance)