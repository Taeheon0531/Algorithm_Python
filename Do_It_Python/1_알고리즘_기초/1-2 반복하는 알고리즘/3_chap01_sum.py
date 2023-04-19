# a부터 b까지 정수의 합 구하기 (for문)

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a    # a와 b를 오름차순으로 정렬 (단일 대입문 사용)

sum = 0
for i in range(a, b +1):
    sum += i       # sum에 i를 더함

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')

"""
두 정수 a와 b를 오름차순으로 정렬한 다음 해당 범위의 모든 정수를 더하는 프로그램
"""

"""
두 값 교환하기
a, b = b, a

< 과정 >
1. 우변의 b, a에 의해 두 값을 압축한 튜플 (b, a) 생성
2. 대입할 튜플 (b, a)를 다시 풀어 b, a로 만든 다음 각각 a와 b에 대입
"""