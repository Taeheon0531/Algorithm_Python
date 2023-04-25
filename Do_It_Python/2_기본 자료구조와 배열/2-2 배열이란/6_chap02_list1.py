#리스트 스캔
# 리스트의 모든 원소를 스캔하기 (원소 수를 미리 파악)

x = ['John', 'George', 'Paul', 'Ringo']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')

"""
원소 수를 len() 함수로 미리 알아내서 0 에서 원소 수 -1 까지 반복
"""