# 세 정수를 입력받아 최댓값 구하기

print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

maximum = a                     # maximum에 a의 값을 대입
if b > maximum: maximum = b     # b 의 값이 maximum보다 크면, maximum에 b의 값을 대입
if c > maximum: maximum = c     # c 의 값이 maximum보다 크면, maximum에 c의 값을 대입
# 8~10 행: 순차구조 sequential structure
# 9~10 행: 선택구조 select structure (조건식)

print(f'최댓값은 {maximum}입니다.')