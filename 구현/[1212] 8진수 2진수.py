'''
[1212] 8진수 2진수 / Bronze 2 / 구현
8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.
'''

# print(bin(int(input(), 8))[2:]) 

oct = int(input(), 8)
bi = list(bin(oct))
del bi[0:2] # list의 0~1번째 요소 삭제
print(''.join(bi))


'''
octal = input() # 314
if octal == '0' : print(0) ; exit(0)
decimal = 0
for i in range(len(octal)) :
    decimal += int(octal[i]) * (8**(len(octal)-1-i))
binary = []
while decimal > 0 :
    binary.append(decimal % 2)
    decimal = decimal // 2

print(*reversed(binary), sep = '')
'''