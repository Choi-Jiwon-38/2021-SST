n = int(input())
score = 0
total_score = 0

for i in range(n):
    test_case = input() 
    for _ in test_case:
        if _ == 'O':
            score += 1
            total_score += score
        else:
            score = 0
            total_score += score
    print(total_score)
    score = 0
    total_score =0