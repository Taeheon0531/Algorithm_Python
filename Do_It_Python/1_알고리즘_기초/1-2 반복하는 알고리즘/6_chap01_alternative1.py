# +와 -를 번갈아 출력하기 1

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(n):
    if i % 2:
        print('-', end='')
    else:
        print('+', end='')

print()

"""
for문 반복은 n번, 나눗셈은 n번, if문 판단은 n번

2가지 문제점 존재
1. for 문을 반복할 때마다 if문 수행
2. 상황에 따라 유연하게 수정하기 어렵다

"""