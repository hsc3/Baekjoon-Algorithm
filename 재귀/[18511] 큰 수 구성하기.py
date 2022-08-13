# [18511] 큰 수 구성하기 | Silver 5 | 재귀
'''
N보다 작거나 같은 자연수 중에서, 집합 K의 원소로만 구성된 가장 큰 수를 출력하는 프로그램을 작성하시오.
K의 모든 원소는 1부터 9까지의 자연수로만 구성된다.
예를 들어 N=657이고, K={1, 5, 7}일 때 답은 577이다.
'''
import sys
input = sys.stdin.readline

def Recur(number):
    global answer

    if int(number) > N: # number가 N보다 커지면 재귀 종료
        return

    answer.append(int(number)) # 숫자 저장
    for num in K:
        Recur(number + num)

if __name__ == "__main__":
    N, len_k = map(int, input().split())
    K = sorted(list(map(str, input().split())), reverse=True)

    answer = []
    Recur("0")
    print(max(answer))