# 백준 : 1021 회전하는 큐

# appendleft(), popleft(), rotate(1), rotate(-1)
import sys
input = sys.stdin.readline
from collections import deque

n, m = list(map(int, input().split()))

q = deque([i for i in range(1, n+1)])  # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

nums = list(map(int, input().split()))

q.index(nums[0]) # nums[0]이 q 안에서 몇번인덱스인가?

cnt = 0  # 총 rotate 횟수
for num in nums:
    while(True):
        
        if q[0] == num: # q의 첫번째인자가 num일떄
            q.popleft()
            break
            
        else:
            
            if q.index(num) >= (len(q) / 2):
                while(q[0] != num):
                    q.rotate(1) # 1 방향(오른쪽) 으로 rotate 
                    cnt += 1
                    
            else:
                while(q[0] != num):
                    q.rotate(-1) # -1 방향(왼쪽) 으로 rotate
                    cnt += 1
                    
print(cnt)