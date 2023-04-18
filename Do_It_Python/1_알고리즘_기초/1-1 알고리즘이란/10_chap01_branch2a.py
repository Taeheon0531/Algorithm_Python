# 실습 1-5의 원래 모습

n = int(input('정수를 입력하세요.: '))

if n == 1:
    print('A')
elif n == 2:
    print('B')
elif n == 3:
    print('C')
else:
    pass

"""
연산자와 피연산자

+ 나 - 등의 기호 : 산술 연살자
연산 대상 : 피연산자

1. 단항 연산자(unary operator) : 피연산자 1개 ex) -a
2. 이항 연산자(binary operator) : 피연산자 2개 ex) a < b
3. 삼항 연산자(ternary operator) : 피연산자 3개 ex) a if b else c

조건 연산자 : if~else 문은 파이썬의 유일한 삼항 연산자
"""