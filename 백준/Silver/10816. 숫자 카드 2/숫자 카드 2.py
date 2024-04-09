import sys
from collections import Counter

input = sys.stdin.readline

def sol():
    n = int(input())
    
    n_list = sorted(list(map(int, input().split())))
    
    m = int(input())
    
    m_list = list(map(int, input().split()))
    
    
    cnt = Counter(n_list)
    
    for i in range(m):
        if m_list[i] in cnt:
            print(cnt[m_list[i]], end = ' ')
        
        else:
            print(0, end = ' ')
    
    
    
sol()