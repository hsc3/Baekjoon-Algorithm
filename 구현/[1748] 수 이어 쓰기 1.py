'''
[1748] 수 이어 쓰기 1 / Silver 4 / 구현, 수학
1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.
1234567891011121314151617181920212223...
이렇게 만들어진 새로운 수는 몇 자리 수일까? 이 수의 자릿수를 구하는 프로그램을 작성하시오.
'''

N = int(input()) # N = 120

res = 0
length = len(str(N)) - 1  # length = 2
while length >= 0 :
    tenSquareNum = 10 ** length # 10의 제곱수. ... 100, 10, 1
    cnt = (N - tenSquareNum) + 1 # 10의 제곱수와 길이가 같은 숫자의 개수
    res += (cnt * (length + 1)) # (length+1) 자리의 숫자 cnt 개를 합산
    length -= 1
    N -= cnt

print(res)