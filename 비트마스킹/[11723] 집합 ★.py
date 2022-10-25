# [11723] 집합 | Silver 5 | https://www.acmicpc.net/problem/11723
import sys
input = sys.stdin.readline

numbers = 0b0

for _ in range(int(input())):
    op = input().split()

    if op[0] == "add":
        numbers = numbers | (1 << int(op[1]) - 1)
        # print("add {} : numbers={}".format(int(op[1]), bin(numbers)))

    elif op[0] == "remove":
        numbers = numbers & ~(1 << int(op[1]) - 1)
        # print("remove {} : numbers={}".format(int(op[1]), bin(numbers)))

    elif op[0] == "check":
        print(1 if numbers & (1 << int(op[1]) - 1) else 0)
        # print("check {}, numbers={}".format(int(op[1]), bin(numbers)))

    elif op[0] == "toggle":
        numbers = numbers ^ (1 << int(op[1]) - 1)
        # print("toggle {} : numbers={}".format(int(op[1]), bin(numbers)))

    elif op[0] == "all":
        numbers = 0b11111111111111111111
        # print("all : numbers={}".format(bin(numbers)))

    elif op[0] == "empty":
        numbers = 0b0
        # print("empty : numbers={}".format(bin(numbers)))


# << 집합 >>
# numbers = set()
# originalSet = set(i for i in range(1, 21))
# for _ in range(int(input())):
#     op = input().split()
#
#     if op[0] == "add" and int(op[1]) not in numbers:
#         numbers.add(int(op[1]))
#     elif op[0] == "remove" and int(op[1]) in numbers:
#         numbers.remove(int(op[1]))
#     elif op[0] == "check":
#         print(1 if int(op[1]) in numbers else 0)
#     elif op[0] == "toggle":
#         if int(op[1]) in numbers:
#             numbers.remove(int(op[1]))
#         else:
#             numbers.add(int(op[1]))
#     elif op[0] == "all":
#         numbers = originalSet.copy()
#     elif op[0] == "empty":
#         numbers.clear()