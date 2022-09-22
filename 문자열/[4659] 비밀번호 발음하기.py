# [4659] 비밀번호 발음하기 | Silver 5 | https://www.acmicpc.net/problem/4659
import sys
input = sys.stdin.readline

def isVowel(c):
    if c in ['a', 'e', 'i', 'o', 'u']:
        return True # 모음
    return False # 자음


answer = []
passwords = []
while True:
    password = input().rstrip()
    if password == "end":
        break

    passwords.append(password)

    # 조건 1 : 모음을 하나라도 포함하는지
    check1 = False
    for i in range(len(password)):
        if isVowel(password[i]):
            check1 = True
            break
    if not check1:
        answer.append(False)
        continue

    # 조건 2 : 3개의 연속된 문자가 모두 모음이거나 자음인지
    check2 = False
    for i in range(len(password)-2):
        if isVowel(password[i]) == isVowel(password[i+1]) == isVowel(password[i+2]):
            check2 = True
            break
    if check2:
        answer.append(False)
        continue

    # 조건 3 : ee, oo를 제외하고 연속된 2개의 문자가 같은지
    exclude = ['e', 'o']
    check3 = False
    for i in range(len(password)-1):
        if password[i] == password[i+1] and password[i: i+1] not in exclude:
            check3 = True
            break
    if check3:
        answer.append(False)
        continue

    answer.append(True)

for i in range(len(answer)):
    if answer[i] == True:
        print("<{}> is acceptable.".format(passwords[i]))
    else:
        print("<{}> is not acceptable.".format(passwords[i]))








