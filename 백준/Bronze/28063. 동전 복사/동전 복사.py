# 백준 : 동전 복사 28063


#      N,1  N,2   ...   N,N
#      N-1,1 N-1,2 ...  N-1, N
    
#      1,1  ...          N,1

import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    x, y = map(int, input().split())
    
    if n == 1:
        print(0)
        
    elif n == 2:
        print(2)
    
    elif (x != 1) & (x != n):
        if (y != 1) & (y != n):
            print(4)
        else:
            print(3)
    else:
        if (y != 1) & (y != n):
            print(3)
        else:
            print(2)
            
            
sol()