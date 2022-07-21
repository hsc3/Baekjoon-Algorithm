# [10996] 별 찍기 (21) / Bronze 2 / 구현
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

N = int(input())
star = [' '] * N
for i in range(0, N, 2) :
    star[i] = '*'

for _ in range(N) :
    print(*star, sep = '')
    print(' ',  *star[:-1], sep = '')

'''
line_1 , line_2 = [], []
for i in range(N) :
    if i % 2 == 0 :
        line_1.append('*')
        line_2.append(' ')
    else :
        line_1.append(' ')
        line_2.append('*')

for _ in range(N) :
    print(*line_1, sep = '')
    print(*line_2, sep = '')
'''