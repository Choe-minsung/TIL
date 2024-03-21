# 백준 : 2512 예산

# 총액 이하에서 모든 요청 분배
# 모두 분배 불가능 시, 정수 상한액
import sys
input = sys.stdin.readline

n = int(input())

price = list(map(int, input().split()))

budget = int(input())


# ===========================================================================================
# case 1) 2중 while문 : 시간초과!

# rest = budget

# price.sort()

# while(True):
#     cnt = 0
#     i = 0
#     while(True):
#         if price[i] <= (budget / n):
#             rest -= price[i]
#             price.pop(i - cnt)
#             i -= 1
#             cnt += 1
#         i += 1
        
#         if (i + cnt) >= (n - 1):
#             break
        
#     if cnt == 0:
#         break

#     budget = rest
#     n = len(price)

# if max(price) > int(rest / (len(price)-cnt)):
#     print(int(rest / (len(price)-cnt)))
# else:
#     print(max(price))
    
# ===========================================================================================
# case 2) 이분탐색 : sol!
start, end = 0, max(price)

while start <= end:         # 이분 탐색
    mid = (start+end) // 2  # 탐색 기준 금액
    total = 0               # 지출금액 합
    
    for i in price:
        if i > mid:
            total += mid
        else:
            total += i
            
    if total <= budget: # 지출 양이 예산 보다 작으면
        start = mid + 1
    else: # 지출 양이 예산 보다 크면
        end = mid - 1
        
print(end)