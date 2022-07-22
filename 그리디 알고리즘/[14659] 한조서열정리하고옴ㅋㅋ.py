# [14659] 한조서열정리하고옴ㅋㅋ / Bronze 1 / 그리디 알고리즘
'''
반고흐#31555가 있는 금강 산맥에는 총 N개의 봉우리가 있고, 모든 봉우리마다 한 명의 활잡이가 서서 월식이 시작되기만을 기다리고 있다.
다만, 애석하게도, 천계에 맥도날드가 생겨 용들이 살이 찐 탓에 용들은 자신보다 낮은 봉우리에 서있는 적들만 처치할 수 있게 되었다.
또한 용들은 처음 출발한 봉우리보다 높은 봉우리를 만나면 그대로 공격을 포기하고 금강산자락에 드러누워 낮잠을 청한다고 한다.
봉우리의 높이는 모두 다르고 모든 용들은 오른쪽으로만 나아가며, 중간에 방향을 틀거나, 봉우리가 무너지거나 솟아나는 경우는 없다.
“달에 마구니가 끼었구나.”
드디어 월식이 시작됐다! 과연 이들 활잡이 중 최고의 활잡이는 누구일까? 최고의 활잡이가 최대 몇 명의 적을 처치할 수 있는지 알아보자.
'''
import sys

N = int(sys.stdin.readline())
mountains = list(map(int, sys.stdin.readline().split()))
answer = 0
while len(mountains) >= answer :
    p = mountains.pop(0)
    count = 0
    for compare in mountains :
        if p > compare :
            count += 1
        else :
            break
    answer = max(answer, count)

print(answer)