n, m = map(int, input().split())

listen = []
for i in range(n):
    listen.append(input())

see = []
for i in range(m):
    see.append(input())

intersection = list(set(listen) & set(see))
intersection = sorted(intersection)

print(len(intersection))
for _ in intersection:
    print(_)
