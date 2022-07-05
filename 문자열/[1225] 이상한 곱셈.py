'''
[1225] 이상한 곱셈 / Bronze 2 / 문자열, 구현
A×B를 계산하다 지겨워진 형택이는 A×B를 새로운 방법으로 정의하려고 한다.
A에서 한 자리를 뽑고 × B에서 임의로 한 자리를 뽑아 곱한다.
의 가능한 모든 조합 (A가 n자리, B가 m자리 수라면 총 가능한 조합은 n×m개)을 더한 수로 정의하려고 한다.
예를 들어 121×34는 1×3 + 1×4 + 2×3 + 2×4 + 1×3 + 1×4 = 28 이 된다.
이러한 형택이의 곱셈 결과를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

memory = [0] * 10 # A의 각각의 숫자 1~9의 곱셈 결과를 저장 (동일연산 제거)
A, B = map(str, input().rstrip().split()) # 123, 45
Alist, Blist = list(map(int, A.rstrip())), list(map(int, B.rstrip())) # [1,2,3], [4,5]

res = 0
for a in Alist :
    if a == 0 : # 0은 계산할 필요 없이 결과가 0이므로 continue
        continue
    elif memory[a] == 0 : # 동일연산이 아직 수행되지 않은 경우
        tmp = 0
        for b in Blist :
            tmp += a * b
        memory[a] = tmp # 메모리에 저장

    res += memory[a] # 메모리에 저장된 곰셈값을 res에 누적

print(res)

