# [16395] 파스칼의 삼각형 | Silver 5 | 다이나믹 프로그래밍
'''
파스칼의 삼각형은 이항계수를 삼각형 형태로 배열한 것인데, 블레즈 파스칼(1623-1662)을 따라 이름 붙여졌다. 단순한 형태로, 파스칼의 삼각형은 다음과 같은 방법으로 만들 수 있다.
1. N번째 행에는 N개의 수가 있다.
2. 첫 번째 행은 1이다.
3. 두 번째 행부터, 각 행의 양 끝의 값은 1이고, 나머지 수의 값은 바로 위 행의 인접한 두 수의 합이다.

정수 n과 k가 주어졌을 때 파스칼의 삼각형에 있는 n번째 행에서 k번째 수를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

def Paskal(layer, arr):
    if layer == n:
        return arr[k-1]

    elif layer == 1:
        return Paskal(layer+1, [1, 1])

    else:
        next_arr = [1 for _ in range(len(arr)+1)]
        for i in range(1, len(arr)):
            next_arr[i] = arr[i-1] + arr[i]

        return Paskal(layer+1, next_arr)

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(Paskal(1, [1]))