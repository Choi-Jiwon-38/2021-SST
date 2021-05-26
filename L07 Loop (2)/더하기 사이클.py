# 1부터 99에 해당하는 숫자를 입력받는다.
n = int(input())  
n_str = str(n)
n_condition = n

# 한 자리수 앞에는 0을 붙여서 두 자리수로 바꾼다.
if n < 10:
    n_str = '0'+str(n)

# 반복문을 구현하기 위해서 try횟수(=t)와 new_num를 0으로 설정한다.
t = 0
new_num = 0

# 더하기 사이클(반복문)
if n_condition == 0 and new_num == 0:
    print('1')
else:
    while n_condition != new_num:
        sum_num = int(n_str[0]) + int(n_str[1])
        sum_num_str = str(sum_num)

        new_num_str = n_str[1] + sum_num_str[len(sum_num_str) - 1]
        new_num = int(new_num_str)
    
        t += 1

        n_str = new_num_str
        n = new_num
    
    # 결과값 출력
    print(t)