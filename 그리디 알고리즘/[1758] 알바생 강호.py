# [1758] 알바생 강호 / Silver 4 / 그리디 알고리즘
'''
스타박스에서는 손님을 8시가 될 때 까지, 문앞에 줄 세워 놓는다. 그리고 8시가 되는 순간 손님들은 모두 입구에서 커피를 하나씩 받고, 자리로 간다. 강호는 입구에서 커피를 하나씩 주는 역할을 한다.
손님들은 입구에 들어갈 때, 강호에게 팁을 준다. 손님들은 자기가 커피를 몇 번째 받는지에 따라 팁을 다른 액수로 강호에게 준다. 각 손님은 강호에게 원래 주려고 생각했던 돈 - (받은 등수 - 1) 만큼의 팁을 강호에게 준다. 만약, 위의 식으로 나온 값이 음수라면, 강호는 팁을 받을 수 없다.
스타박스 앞에 있는 사람의 수 N과, 각 사람이 주려고 생각하는 팁이 주어질 때, 손님의 순서를 적절히 바꿨을 때, 강호가 받을 수 잇는 팁의 최댓값을 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline
'''
N = int(input()) # 줄서 있는 사람의 수
money = sorted([int(input()) for _ in range(N)], reverse=True)

answer = 0
# 많은 금액을 주는 손님을 우선 순위로 받는다.
for i in range(len(money)):
    tip = money[i] - i
    if tip > 0:
        answer += tip

print(answer)
'''
# tip = money - index
tips = [m-i for i, m in enumerate(sorted(list(int(input()) for _  in range(int(input()))), reverse=True))]
answer = 0
for tip in tips:
    if tip > 0:
        answer += tip
print(answer)