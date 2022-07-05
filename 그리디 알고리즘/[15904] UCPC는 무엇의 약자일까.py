'''
[15904] UCPC는 무엇의 약자일까 / Silver 5 / 그리디, 문자열
첫 번째 줄에 입력으로 주어진 문자열을 적절히 축약해 "UCPC"로 만들 수 있으면 "I love UCPC"를 출력하고, 만들 수 없으면 "I hate UCPC"를 출력한다.
'''
import sys
input = sys.stdin.readline

str = list(input().rstrip())
ucpc = True

for alphabet in ['U', 'C', 'P', 'C'] :
    if alphabet in str :
        str = str[str.index(alphabet)+1:] # 다음부터 해당 이니셜이 위치한 뒤의 문자열만 비교한다.(U,C,P,C 각 이니셜을 순서대로 비교할 수 있다)
    else :
        ucpc = False
        break

print("I love UCPC" if ucpc else "I hate UCPC")




