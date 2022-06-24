'''
[1541] 잃어버린 괄호 / Silver 2 / 문자열, 수학
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline
# ex) 55-50+40+20-50
string = list(input().rstrip().split('-')) # [55, 50+40+20, 50]
res = 0

for i in range(len(string)) :
    numbers = list(map(int, string[i].split('+')))
    # i=0 : numbers = [55] --> 55
    # i=1 : numbers = [50,40,20] --> -110
    # i=2 : numbers = [50] --> -50

    if i == 0 :
        res += sum(numbers) # string의 첫번째 원소에 위치한 숫자들은 무조건 양수이다.
    else :
        res -= sum(numbers) # 이후의 원소에 위치한 숫자들은 모두 더한 후 빼줄 수 있다. (음수로 만들 수 있다.)

print(res)