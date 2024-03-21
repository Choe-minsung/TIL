import sys
input = sys.stdin.readline

n = int(input())
    
temp = []
for i in range(n):
    temp.append(int(input()))
    
import heapq as h

val = []
for i in range(n):
    if temp[i] != 0:
        h.heappush(val, (-1) * temp[i]) # -를 붙여 push
    else:
        if len(val) == 0:
            print(0)
        else:
            result = h.heappop(val) # min값 pop
            print((-1) * result) # 다시 -를 붙여 반환하면 max값 출력o