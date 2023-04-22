# 각 배열 원소의 최댓값을 구해서 출력하기 (튜플, 문자열, 문자열 리스트)

from max1 import max_of

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}의 최댓값은 {max_of(t)}입니다.')
print(f'{s}의 최댓값은 {max_of(s)}입니다.')
print(f'{a}의 최댓값은 {max_of(a)}입니다.')

"""
튜플 t는 정수와 실수 원소가 섞여있지만 최댓값 7 출력
s는 string 이라는 문자 가운데 가장 큰 문자 코드인 t 출력
a는 문자열 리스트(모든 원소가 str형 문자열인 list)로, 사전 순으로 가장 큰 문자열인 FLAC을 출력
"""