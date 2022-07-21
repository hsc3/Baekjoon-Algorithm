'''
[2745] 진법 변환 (1) / Bronze 2 / 구현
B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
'''
N, B = input().split()

res = 0

for i in range(len(N)) :
    if N[i].isalpha() :
        num = ord(N[i]) - 55
    else : 
        num = int(N[i])

    res += num * (int(B) ** (len(N)-i-1))

print(res)

'''
N, B= map(str, input().split())
B = int(nota)
print(int(N, B))
'''