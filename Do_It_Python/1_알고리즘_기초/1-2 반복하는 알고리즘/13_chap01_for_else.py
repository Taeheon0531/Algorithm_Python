# 10~99 사시의 난수 n개 생성하기 (13이 나오면 중단)

import random

n = int(input('난수의 개수를 입력하세요.: '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r == 13:
        print('\n프로그램을 중단합니다.')
        break
else:
    print('\n난수 생성을 종료합니다.')


"""
else 문이 뒤따르는 for 문

13이 생성될 경우 break문으로 반복문을 강제 종료
13 이후 난수는 출력되지 않고 else문도 실행되지 않음

만약 13이 생성되지 안으면 반복이 끝난 다음 else문이 실행되어 '난수 생성을 종료합니다.' 를 출력

"""