'''
[1427] 소트인사이드
Silver 5 | 정렬, 문자열
수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
'''
print(*sorted(list(map(int, input())), reverse = True), sep = '')
#numbers = list(map(int, input().rstrip()))
#print(*sorted(numbers, reverse = True), sep = '')