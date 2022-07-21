'''
[1475] 방 번호 / Silver 5 / 구현
다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.
다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 
다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. 
(6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)
'''
num = list(map(int, input().rstrip()))
dict = {}
for n in num :
    if n == 6 : n = 9
    dict[n] = dict.get(n, 0) + 1

dict = list(sorted(dict.items(), key=lambda x : (-x[1],x[0])))
if dict[0][0] == 9 :
    if dict[0][1] % 2 == 0 :
        print(dict[0][1] // 2)
    else :
        print(dict[0][1] // 2 + 1)
else : 
    print(dict[0][1])

'''
n = input()
lst = [0]*9
for i in n:
    if i == '9':
        lst[6] += 1
    else:
        lst[int(i)] += 1
lst[6] = (lst[6]+1)//2
print(max(lst))
'''