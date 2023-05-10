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