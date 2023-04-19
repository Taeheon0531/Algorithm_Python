# 1부터 n까지 정수의 합 구하기 2 (for문)

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요.: '))

sum = 0
for i in range(1, n + 1):
    sum += i                    #sum에 i를 더함

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

"""
변수가 하나만 있을 때는 while 문보다 for 문을 사용하는 것이 좋음
"""

"""
range() 함수

1. range(n) : 0 이상 n 미만인 수를 차례로 나열하는 수열
2. range(a, b) : a 이상 b 미만인 수를 차례로 나열하는 수열
3. range(a, b, step) : a 이상 b 미만인 수를 step 간격으로 나열하는 수열

=> 이터러블 객체 (반복할 수 있는 객체)
"""