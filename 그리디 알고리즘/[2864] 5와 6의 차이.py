# [2864] 5와 6의 차이 / Bronze 2 / 그리디 알고리즘
'''
상근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고, 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.
두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다. 이때, 상근이가 구할 수 있는 두 수의 가능한 합 중, 최솟값과 최댓값을 구해 출력하는 프로그램을 작성하시오.
'''
def readableCase(n1, n2) :
    n1_case = []
    n2_case = []
    n1_case.append(int(n1.replace('5', '6')))
    n1_case.append(int(n1.replace('6', '5')))
    n2_case.append(int(n2.replace('5', '6')))
    n2_case.append(int(n2.replace('6', '5')))

    return n1_case, n2_case

n1, n2 = input().split()
n1_case, n2_case = readableCase(n1, n2)
print(min(n1_case) + min(n2_case), max(n1_case) + max(n2_case))