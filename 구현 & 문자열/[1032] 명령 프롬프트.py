'''
[1032] 명령 프롬프트 | 구현, 문자열
검색 결과가 먼저 주어졌을 때, 패턴으로 뭘 쳐야 그 결과가 나오는지를 출력하는 문제이다. 
패턴에는 알파벳과 "." 그리고 "?"만 넣을 수 있다.
'''
n = int(input())
s = [set() for _ in range(50)] # 파일이름의 최대 길이 : 50

for _ in range(n) :
    tmp = input()
    for i in range(len(tmp)) :
        s[i].add(tmp[i]) # 문자열의 각 문자를 집합에 저장.

answer = ""
for a in s :
    if len(a) == 0 : # 문자열의 길이를 넘어서면 종료.
        break
    elif len(a) == 1 : # 입력받은 모든 문자열의 자리 문자가 동일한 경우.
        answer += a.pop()
    else : # 문자가 동일하지 않은 경우. (set의 중복된 문자를 저장하지 않는 특징 이용)
        answer += "?"

print(answer)