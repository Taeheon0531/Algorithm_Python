# 세 정수의 최댓값 구하기

def max3(a, b, c):
    """a,b,c의 최댓값을 구하여 반환"""
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum                  #최댓값 반환

print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')
print(f'max3(3, 2, 2) = {max3(3, 2, 2)}')
print(f'max3(3, 1, 2) = {max3(3, 1, 2)}')
print(f'max3(3, 2, 3) = {max3(3, 2, 3)}')
print(f'max3(2, 1, 3) = {max3(2, 1, 3)}')
print(f'max3(3, 3, 2) = {max3(3, 3, 2)}')
print(f'max3(3, 3, 3) = {max3(3, 3, 3)}')
print(f'max3(2, 2, 3) = {max3(2, 2, 3)}')
print(f'max3(2, 3, 1) = {max3(2, 3, 1)}')
print(f'max3(2, 3, 2) = {max3(2, 3, 2)}')
print(f'max3(1, 3, 2) = {max3(1, 3, 2)}')
print(f'max3(2, 3, 3) = {max3(2, 3, 3)}')
print(f'max3(1, 2, 3) = {max3(1, 2, 3)}')

"""
복합문의 구조
if 나 while = 헤더 ( :콜론으로 끝나는 경우)
헤더의 콜론 뒤에는 스위트(suite) 가 이어짐

if식 : 반드시 1개의 스위트 필요
elif식 : 없거나, 있으면 n개 가능
else식 : 없거나, 있으면 1개 가능
"""

"""
알고리즘이란:
어떠한 문제를 해결하기 위해 정해 놓은 일련의 절차

올바른 알고리즘:
어떠한 경우에도 실행 결과가 똑같이 나오는 것
"""

"""
복합문 작성시 규칙

1. 반드시 행마다 같은 수준으로 들여쓰기 (PEP 8: 공백 4개로 들여쓰기)

2. 스위트가 단순문이면 헤더와 같은 행에 둘 수 있음
ex) if a<b: min2 = a

3. 단순문이 2개 이상이면 ;(세미콜론) 으로 구분하여 같은 행에 둘 수 있음 (마지막엔 두든 말든 상관 x)
ex) if a< b: min2 = a; max2 = b

4. 스위트가 복합문이면 헤더와 스위트는 같은 행에 포함시킬 수 없음
ex) if a < b: if c < d: x = u : 불가능
"""