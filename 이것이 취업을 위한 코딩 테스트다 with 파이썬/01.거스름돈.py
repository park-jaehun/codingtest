n = 2000
count = 0
ls = [500, 100, 50]
if n < 10:
        print(n,"원 거스름몬입니다.")

while n >= 10:
        if n >= 500:
                count = (n//500)
                n = (n % 500)
        elif n >= 100:
                count = count + (n//100)
                n = (n % 100)
        else:
                count = count + (n//10)
                n = (n % 10)

print(count,"거스름돈 입니다.")

# 1260 % 500 ------- 몫에 따른 동전 개수