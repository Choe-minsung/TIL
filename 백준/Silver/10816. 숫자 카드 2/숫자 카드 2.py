import sys
from collections import Counter

input = sys.stdin.readline

def sol():
    n = int(input())
    
    n_list = sorted(list(map(int, input().split())))
    
    m = int(input())
    
    m_list = list(map(int, input().split()))
    
    
    cnt = Counter(n_list) # Counter 로 인자 갯수세기
    
    for i in range(m):
        if m_list[i] in cnt: # n_list 인자가 m_list에 있으면
            print(cnt[m_list[i]], end = ' ') # cnt 에 저장 된 해당 요소의 갯수 출력
        
        else:
            print(0, end = ' ') # 없으면 0 출력
    
    
    
sol()