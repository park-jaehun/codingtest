# 자세한 문제 풀이 .....
# -*- coding: utf-8 -*-

# 현재 나이트의 위치 입력 받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1


# 나이트가 이동할 수 있는 8가지 방향 정의
result = 0
steps = [(1,-2),(1,2),(-1,-2),(-1,2),(-2,-1),(-2,1),(2,-1),(2,1)]
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
        result += 1

print(result)

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인



