# 1~12까지 8을 건너뛰고 출력하기 1

for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')

print()

"""
반복문 건너뛰기

=> 8 이 나오면 건너뚜미

** 그러나 이 방법은 비효율적
"""