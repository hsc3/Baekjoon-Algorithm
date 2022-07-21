'''
[4458] 첫 글자를 대문자로 / Bronze 2 / 문자열
문장을 읽은 뒤, 줄의 첫 글자를 대문자로 바꾸는 프로그램을 작성하시오.
'''
# str과 tuple 형은 수정이 불가능하다.
# str의 경우, list로 변환 후에 수정해야 한다. 혹은 replace 메서드 이용

n = int(input())
ans = []

for _ in range(n) :
    tmp = list(input().rstrip())
    if tmp[0].islower() :
        tmp[0] = tmp[0].upper()
    ans.append(''.join(tmp))

print(*ans, sep = '\n')