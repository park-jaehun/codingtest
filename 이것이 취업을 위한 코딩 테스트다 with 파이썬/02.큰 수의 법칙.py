n,m,k = map(int, input().split())
data = list(map(int, input().split()))
if n == len(data):
    data = sorted(data)
    leng = len(data)-1
    first = data[leng]
    second = data[leng - 1]
    if (m != 0) & (k!=0):
        first_result = first * (m//k) * k
        second_count = m%k
        second_result = second * second_count
        print(first_result + second_result)
    elif (k==0):
        print(sum(data))
    else:
        print("0")
else:
    print("입력을 다시 하십쇼")
