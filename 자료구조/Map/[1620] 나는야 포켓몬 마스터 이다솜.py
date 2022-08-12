'''
[1620] 나는야 포켓몬 마스터 이다솜 | Silver 4 | 자료구조 (Map)
Q : N개의 포켓몬 정보를 저장하고 M개의 퀴즈를 맞추시오.
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_to_pokemon = {}
pokemon_to_num = {}
for n in range(1, N+1) :
    pokemon_name = input().rstrip()
    num_to_pokemon[str(n)] = pokemon_name
    pokemon_to_num[pokemon_name] = n
     

for _ in range(M) :
    question = input().rstrip()
    if ord(question[0]) <= 57 : # num -> name
        print(num_to_pokemon[question])
    else : # name -> num
        print(pokemon_to_num[question])

'''
N, M = map(int, input().split())
num_to_str = dict()
str_to_num = dict()

for i in range(1, N+1):
    name = input().strip()
    num_to_str[i] = name
    str_to_num[name] = i

for _ in range(M):
    temp = input().strip()
    if temp.isnumeric():
        print(num_to_str[int(temp)])
    elif temp.isalpha():
        print(str_to_num[temp])
'''