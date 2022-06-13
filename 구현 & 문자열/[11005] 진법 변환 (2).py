# [11005] 진법 변환 (2)
# Bronze 1 >> 수학, 구현, 문자열

N, B = map(int, input().split()) 
res = ''

while N :
    d = N % B
    N //= B
    
    if d >= 10 :
        res = chr(d+55) + res
    else :
        res = str(d) + res

print(res)
