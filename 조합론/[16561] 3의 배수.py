# [16561] 3의 배수 | Bronze 2 | 조합론
from itertools import product, permutations, combinations

'''
윤영이는 3의 배수 마니아이다. 그는 모든 자연수를 3개의 3의 배수의 자연수로 분해하는 것을 취미로 가지고 있다.
문득 그는 자신에게 주어진 수를 3개의 3의 배수로 분리하는 경우의 수가 몇 개인지 궁금해졌다.

즉, 임의의 3의 배수 자연수 n이 주어졌을 때, 해당 수를 3의 배수의 자연수 3개로 분리하는 방법의 개수를 출력해라.
단 분해한 수의 순서가 다르면 다른 방법으로 간주한다. 예를 들어 12 = 3 + 6 + 3 과 12 = 3 + 3 + 6 은 다른 방법이다.
'''
# 9 -> 3+3+3 (3 * 3) 1
# 12 -> 3+3+6 , 3+6+3, 6+3+3 (3 * 4) 3
# 15 -> 3+3+9 , 3+9+3, 9+3+3, 3+6+6, 6+3+6, 6+6+3 (3 * 5) 6
# 18 -> 3+3+12, 3+12+3, 12+3+3, 3+6+9, 3+9+6, 6+3+9, 6+9+3, 9+3+6, 9+6+3, 6+6+6 (3 * 6) 10

n = int(input())

answer = 0
for i in range(3, n+1, 3):
    for j in range(3, n-i-2, 3):
        answer += 1 # 숫자 2개를 정하면 나머지 숫자는 알아서 정해진다.
print(answer)

# n = int(input())
# answer = 0
# for small in range(3, (n//3)+1, 3):
#     for mid in range(small, (n-small)//2+1, 3):
#         numbers = set([small, mid, n-(small+mid)])
#         if len(numbers) == 3:
#             answer += 6
#         elif len(numbers) == 2:
#             answer += 3
#         else:
#             answer += 1
#
# print(answer)