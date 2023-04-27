"""
** 보초법

단순한 판단의 반복 -> 종료조건을 검사하는 비용(cost) 문제

=> 보초법 (sentinel method)

검색하고자 하는 키 값을 배열의 맨 끝에 저장 (저장하는 값을 보초 (sentinel)이라고 함)

보초법을 이용하면 
선형검색의 종료 조건 (검색할 값을 찾지 못하고 배열의 맨 끝을 지나갔습니까?) 는 판단할 필요가 없게됨

따라서 반복을 종료하는 판단 횟수르 줄이는 역할을 함
"""

# 선현 검색 알고리즘을 보초법으로 수정

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    """시퀀스 seq에서 key와 일치하는 원소를 선형 검색 (보초법)"""
    a = copy.deepcopy(seq)  # seq를 복사
    a.append(key)           # 보초 key를 추가

    i = 0
    while True:
        if a[i] == key:
            break           # 검색에 성공하면 while ansdmf whdfy
        i += 1
    return -1 if i == len(seq) else i

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: ')) # num 값을 입력
    x = [None] * num                        # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력하세요.: '))    # 검색할 키 ky를 입력받기

    idx = seq_search(x, ky)                    # 키 ky 값과 같은 원소를 x에서 검색

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')