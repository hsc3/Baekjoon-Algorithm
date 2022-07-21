# [2587] 대표값2 / Bronze 2 / 구현
# 다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.

numbers = sorted([int(input()) for _ in range(5)])
print(sum(numbers)//5, numbers[2])