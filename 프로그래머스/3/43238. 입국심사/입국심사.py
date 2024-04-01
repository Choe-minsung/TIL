# 이분탐색 : O(log n * t)

# 1 <= n <= 10**9
# 1 <= times[i] <= 10**9
# 1 <= len(times) <= 10**5

def solution(n, times):
#     answer = 0
    
#     times.sort()
    
    start, end = 1, min(times) * n  # Testcase의 탐색범위 : 1 ~ 42
    
    while(start <= end):
        mid = (start + end) // 2
        
        cnt = 0
        
        for i in times:
            cnt += mid // i  # Testcase에서 (43 // 7) + (43 // 10)...
            
        if cnt < n:
            start = mid + 1
        else:               # cnt == n 일때도 end부 조정!
            end = mid - 1
            
        
    return start   
    
