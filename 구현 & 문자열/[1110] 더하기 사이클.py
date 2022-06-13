# [1110] 더하기 사이클
# Bronze 1 >> 구현, 수학

origNum = int(input()) # 0 <= number <= 99 (26)
num1 = origNum 
res = 0

while True:
    res += 1
    tmp = num1 // 10 + num1 % 10 # tmp = 2+6 = 8
    num1 = (num1 % 10) * 10 + (tmp % 10) # num1 = 68
    if num1 == origNum: break

print(res)