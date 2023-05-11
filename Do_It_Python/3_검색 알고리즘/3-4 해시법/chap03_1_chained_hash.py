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
"""