# 체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key: Any, Value: Any, next: Node) -> None:
        """초기화"""
        self.key = key  #키
        self.value = Value  #값
        self.next = next    #뒤쪽 노드를 참조

class ChainedHash:
    """체인법으로 해시 클래스 구현"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity    # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity # 해시 테이블(리스트)을 선언

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key) # 검색하는 키의 해시값
        p = self.table[hash]        # 노드를 주목

        while p is not None:
            if p.key == key:
                return p.value      # 검색 성공
            p = p.next              # 뒤쪽 노드를 주목

        return None                 # 검색 실패
    
    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key) # 추가하는 key의 해시값
        p = self.table[hash]        # 노드를 주목

        while p is not None:
            if p.key == key:
                return False        # 추가 실패
            p = p.next              # 뒤쪽 노드를 주목

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp     # 노드를 추가
        return True                 # 추가 성공



"""
Node 클래스 만들기

Node 클래스: 개별 버킷 (3가지 필드)
- key: 키(임의의 자료형)
- value: 값(임의의 자료형)
- next: 뒤쪽 노드를 참조(Node형)

=> 키와 값이 짝을 이루는 구조

키에 해시 함수를 적용하여 해시값을 구함


__init__() 함수는 Node형 인스턴스를 초기화 => key, value, next를 전달받아 각각 self.에 대입

"""

"""
ChainedHash 해시 클래스 만들기
- 2개의 필드로 구성
1. capacity : 해시 테이블의 크기(배열table의 원소 수)를 나타냄
2. table    : 해시 테이블을 저장하는 list형 배열을 나타냄

__init__() 함수로 초기화하기
- 빈 해시 테이블을 생성
capacity에 전달받는 것은 해시 테이블의 크기
원소 수가 capacity 인 list형의 배열 tale을 생성하고 모든 원소를 None으로 함
해시 테이블의 각 버킷은 맨 앞부터 talbe[0], talbe[1], ... , table[capacity-1]
__init__() 함수가 호출된 직후 배열 table의 모든 원소는 None 이고 전체 버킷은 빈 상태

hash_value() 해시함수 만들기
- 인수 key에 대응하는 해시값을 구함


[해시와 해시 함수 알아보기]

해시 함수로 인덱스를 찾는 것 => 시간복잡도 O(1) (충돌이 없을 때)
- 해시테이블을 충분히 크게 만들면 충돌 발생을 억제 가능 but 메모리 낭비
따라서 해시 테이블의 크기를 소수를 선호

1. key가 int형인 경우
: key를 해시의 크기 capacity로 나눈 나머지를 해시값으로 지정

2. key가 int형이 아닌 경우
: 표준 라이브러리로 형 변환
- sha256 알고리즘 : hashlib에서 제공
- encode() 함수 : hashlib.sha26에는 바이트 문자열의 인수를 전달해야하므로 key를 str문자열로 변환한 뒤 
                    문자열은 encode() 함수에 전달하여 바이트 문자열 생성
- hexdigest() 함수 : sha256 알고리즘에서 해시값을 16진수 문자열로 꺼냄
- int() 함수 : hexdigest() 함수로 꺼낸 문자열을 16진수 문자열로 하는 int형으로 변환


** 키로 원소를 검색하는 search() 함수
1. 해시 함수를 사용하여 키를 해시값으로 변환
2. 해시값을 인덱스로 하는 버킷에 주목
3. 버킷이 참조하는 연결 리스트를 맨 앞부터 차례로 스캔. 키와 같은 값이 발견되면 검색에 성공하고,
원소의 맨 끝까지 스캔해서 발견되지 않으면 검색에 실패 
"""

"""
** add() 함수
키가 key 이고 값이 value인 원소를 추가

ex) 13 추가하기
13의 해시값: 0
table[0] : None
노드를 새로 생성하고, 그 노드에 대한 참조를 table[0]에 대입

ex) 46 추가하기
46의 해시값: 7
table[7] : 20, 33을 연결한 연결리스트에 대한 참조가 저장되어 있음
리스트 안에 46은 존재하지 않으므로 연결리스트의 맨 앞에 46을 추가
-> 46을 저장하는 노드를 새로 생성하고, 그 노드에 대한 참조를 table[7]에 대입
추가한 노드의 뒤쪽 포인터인 next가 20을 저장한 노드를 주목하도록 업데이트

정리
1. 해시함수를 사용하여 키를 해시값으로 변환
2. 해시값을 인덱스로 하는 버킷에 주목
3. 버킷이 참조하는 연결리스트를 맨 앞부터 차례로 선형 검색. 키와 같은 값이 발견되면 키가 이미 등록된 경우이므로 추가에 실패
원소의 맨 끝까지 발견되지 않으면 해시값인 리스트의 맨 앞에 노드를 추가


** 원소를 삭제하는 remove() 함수
: 키가 key인 원소를 삭제

ex) 69 삭제
69의 해시값: 4
table[4]의 버킷에 저장되어 있는 참조하는 곳의 리스트를 선형 검색하여 69 발견
이 노드의 뒤쪽 노드는 17을 저장
따라서 17을 저장한 노드에 대한 참조를 table[4] 버킷에 대입하면 노드가 삭제됨

정리
1. 해시 함수를 사용하여 키를 해시값으로 변환
2. 해시값을 인덱스로 하는 버킷에 주목
3. 버킷이 참조하는 연결리스트를 맨 앞부터 차례로 선형 검색. 키와 같은 값이 발견되면 그 노드를 리스트에서 삭제.
그렇지 안흥면 삭제에 실패.
"""