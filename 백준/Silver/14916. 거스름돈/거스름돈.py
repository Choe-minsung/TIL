# 백준 14916 : 거스름돈

# 2원 or 5원

n = int(input())
i = 0
cnt = -1
while((n - (5*i)) >= 0):
    if (n - (5*i)) % 2 == 0:
        cnt = i + ((n - (5 * i)) // 2)
    
    i += 1

print(cnt)