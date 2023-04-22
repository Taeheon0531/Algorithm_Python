# 10진수 정숫값을 입력받아 2~36 진수로 변환하여 출력하기 (수정)

def card_conv(x: int, r: int) -> str:
    """정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""

    d = ''          # 변환 후의 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x)) # 변환하기 전의 자릿 수

    print(f'{r:2} : {x:{N}d}')
    while x > 0:
        print('  +' + (n + 2) * '-')
        if x // r:
            print(f'{r:2} : {x // r:{n}d} ... {x % r}')
        else:
            print(f'    {x // r:{n}d} ... {x % r}')
        d += dchar [x % r]          # 해당하는 문자를 꺼내 결합
        x //= r

    return d[::-1]      # 역순으로 변환