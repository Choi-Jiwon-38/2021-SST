n = int(input())

for i in range(n):
    temp = list(map(int, input().split()))
    count = 0
    sum = 0
    for j in range(1, len(temp)):
        sum += temp[j]

    average = sum / temp[0]

    for z in range(1, len(temp)):
        if temp[z] > average:
            count += 1

    average_temp_per = (count / temp[0]) * 100
    print(f"{round(average_temp_per, 3):.3f}%")