import sys
n = int(input())
enrolment = set()
for line in sys.stdin:
    a, b = line.strip.split()
    if b == "enter":
        enrolment.add(b)
    else:
        enrolment.remove(b)

