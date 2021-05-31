n, m = map(int, input().split())
min_result = []
for i in range(n):
    # 해당  row의 개수만큼 리스트가 형성됨
    ls = list(map(int, input().split()))
    # row가 생길 때마다 min을 리스트로 저장
    min_result.append(min(ls))
# 리스트의 최소값으 출력
print(max(min_result))
