# a 부터 b 까지 정수의 합 구하기 2

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i                #sum에 i를 더함

print(f'{b} = ', end='')
sum += b                    #sum에 b를 더함

print(sum)

"""
for문 반복은 n-1번
if문 판단은 0번
"""

"""
두 값 교환하기 2

임시용 변수 t 이용

1. a값을 t에 저장
2. b값을 a에 대입
3. t에 저장한 처음 a값을 b에 대입
"""