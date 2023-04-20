# 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기

area = int(input('직사각형의 넓이를 입력하세요.: '))

for i in range(1, area + 1):
    if i * i > area: break                  # i*i가 area 를 초과하면 for문 강제 종료
    if area % i: continue                   # area가 i로 나누어 떨어지지 않으면 for 문의 다음 반복으로 진행
    print(f'{i} x {area // i}')             # i 와 area // i 의 값을 짧은 변, 긴 변의 순서롤 출력