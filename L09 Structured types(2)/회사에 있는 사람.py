n  = int(input())

corp = dict()
for i in range(n):
    name, stat = input().split()
    if stat == 'enter':
        corp[name] = True
    else:
        del corp[name]

print("|n".join(sorted(corp.keys(), reverse=True)))