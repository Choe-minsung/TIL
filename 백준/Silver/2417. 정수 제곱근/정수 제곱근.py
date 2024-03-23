# 백준 : 정수 제곱근 2417

import sys
input = sys.stdin.readline

def sol():
    n = int(input())
    
    start = 0
    end = n
    
    result = 0
    
    while(start <= end):
        mid = (start + end) // 2
        
        if mid**2 < n:
            start = mid + 1
        
        else:
            result = mid
            end = mid - 1
            
    print(result)
            
        
        
sol()



