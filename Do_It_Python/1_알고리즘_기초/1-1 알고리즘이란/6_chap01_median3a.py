# 세 정수를 입력받아 중앙값 구하기 2

def med3(a, b, c):
    '''a, b, c의 중앙값을 구하여 반환(다른 방법)'''
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c
#생략

"""
이 경우 a 와 b 의 비교를 이미 마친 상태에서 다시 비교하게 되므로 효율적이지 않음
"""