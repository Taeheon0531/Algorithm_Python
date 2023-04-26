# prime number = 소수
# composite number = 합성수

# 1000 이하의 소수를 나열하기
counter = 0     # 나눗셈 횟수를 카운트

for n in range(2, 1001):
    for i in range(2, n):
        counter += 1
        if n % i == 0:      # 나누어 떨어지면 소수가 아님
            break           # 반복 불필요
    else:
        print(n)
print(f'나눗셈을 실행한 횟수: {counter}')

"""
n이 소수일 때: for 문은 마지막까지 실행 -> else문을 실행하여 n값 출력
n이 합성수일 때: for 문 중단

=> n이 2와 3으로 나누어 떨어지지 않는다면 2x2인 4와 2x3인 6으로도 나누어 떨어지지 않음. 즉, 불필요한 나눗셈 실행중

=> 정수 n이 소수인지 여부는 2부터 n-1까지 어떤 소수로도 나누어 떨어지지 않는 것을 판단하면 됨
"""