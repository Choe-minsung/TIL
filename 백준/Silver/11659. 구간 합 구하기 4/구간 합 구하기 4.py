import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    arr_sum = [0]
    
    for i in range(n):
        arr_sum.append(arr_sum[i] + arr[i])
    
    for _ in range(m):
        i, j = map(int, input().split())
        print(arr_sum[j] - arr_sum[i-1])
        
    return None
        
        
solve()