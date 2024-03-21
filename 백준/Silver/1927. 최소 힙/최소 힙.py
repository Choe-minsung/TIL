import sys
import heapq as h
input = sys.stdin.readline

n = int(input())

temp = []
for i in range(n):
    temp.append(int(input()))
    
val = []
for i in range(n):
    if temp[i] != 0:
        h.heappush(val, temp[i])
        
    else:
        if len(val) == 0:
            print(0)
        else:
            print(h.heappop(val))