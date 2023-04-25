# 배열 원소의 최댓값 구하기
"""
maximum = a[0]
if a[1] > maximum: maximum = a[1]
if a[2] > maximum: maximum = a[2]
def max_of(a):
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
"""
"""
스캔(scan) : 배열 원소를 하나씩 차례로 주목하여 살펴보는 방식
"""

# 시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    '''시퀀스형 a 원소의 최댓값을 반환'''
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 리스트를 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

    print(f'최댓값은 {max_of(x)}입니다.')

"""
주석과 자료형 힌트
Ex) from typing import Any, Sequence

Any: 제약이 없는 임의의 자료형
Sequecne: 시퀀스형 (리스트형, 바이트 배열형, 문자열형, 튜플형, 바이트열형 등)

따라서 두 자료형을 사용하여 max_of() 함수를 정의하면
1. 건네받는 매개변수 a의 자료형은 Sequence
2. 반환하는 것은 임의의 자료형인 Any

"""

"""
재사용할 수 있는 모듈 작성하기

모듈: 하나의 스크립트 프로그램
.py를 포함하지 않는 파일의 이름 자체를 모듈 이름으로 사용

if __name__ == '__main__'

모듈 이름을 나타내는 변수: __name__

작성규칙
1. 스크립트 프로그램이 직접 실행될 대 변수 __name__ 은 '__main__'
2. 스크립트 프로그램이 임포트 될 때 변수 __name__은 원래의 모듈 이름

"""