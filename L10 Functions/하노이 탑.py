def h(n, start, middle, end):
    if n == 1:
        print(f"{start} {end}")
    else:
        h(n-1, start, end, middle)
        h(1, start, middle, end)
        h(n-1, middle, start, end)

n = int(input())
count = 2**n -1


print(count)
if n <= 20:
    h(n, 1, 2, 3)