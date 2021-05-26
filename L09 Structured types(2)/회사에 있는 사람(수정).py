import sys
n = int(input())
enrolment = set()


for line in sys.stdin:
    a, b = line.strip().split()
    if b == "enter":
        enrolment.add(a)
    else: # b == "leave"
        enrolment.remove(a)

rest = sorted(enrolment, reverse=True)
for _ in rest:
    print(_)