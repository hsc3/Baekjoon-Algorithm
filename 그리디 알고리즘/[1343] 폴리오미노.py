# [1343] 폴리오미노 | Silver 5 | 그리디 알고리즘
'''
민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB
이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, '.'는 폴리오미노로 덮으면 안 된다.
폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오. 첫째 줄에 사전순으로 가장 앞서는 답을 출력한다. 만약 덮을 수 없으면 -1을 출력한다.
'''
import sys
input = sys.stdin.readline

board = input().replace('XXXX', 'AAAA').replace('XX', 'BB')
print(-1 if 'X' in board else ''.join(board))

#
# cursor = 0
# while cursor < len(board):
#     if board[cursor] == '.': # '.'은 덮지 않고 건너뛴다.
#         cursor += 1
#     elif cursor + 4 <= len(board) and '.' not in board[cursor:cursor+4]: # AAAA로 덮는다.
#         board[cursor:cursor+4] = ['A'] * 4
#         cursor += 4
#     elif cursor + 2 <= len(board) and '.' not in board[cursor:cursor+2]: # BB로 덮는다.
#         board[cursor:cursor+2] = ['B'] * 2
#         cursor += 2
#     else: # 덮을 수 없는 경우
#         print(-1)
#         exit(0)
#
# print(*board, sep='')

