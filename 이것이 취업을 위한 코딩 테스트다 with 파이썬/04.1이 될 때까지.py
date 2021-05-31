n,m = map(int, input().split())
count = 0
while n >= 1:
    if n%m == 0:
        count += 1
        n = n//m
    else:
        count += 1
        n = (n-1)
print(count)