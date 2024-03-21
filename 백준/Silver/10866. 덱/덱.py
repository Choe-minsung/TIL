# 백준 BOJ : 10866 덱

# 정수저장 덱 구현

# push_front X: 정수 X를 덱 앞에 넣기
# push_back X: 정수 X를 덱 뒤에 넣기
# pop_front: 덱의 가장 위에 있는 정수를 빼고 그 수를 출력. 덱에 들어있는 정수가 없는 경우에는 -1을 출력.
# pop_back: 덱의 가장 뒤에 있는 정수를 빼고 그 수를 출력. 덱에 들어있는 정수가 없는 경우에는 -1을 출력.
# size: 덱에 들어있는 정수의 개수를 출력.
# empty: 덱이 비어있으면 1, 아니면 0을 출력.
# front : 덱 맨 앞의 정수 출력, 없으면 -1 출력
# back : 덱 맨 뒤의 정수 출력, 없으면 -1 출력

import sys
input = sys.stdin.readline

from collections import deque 

n = int(input())

command = []
for i in range(n):
    command.append(input().split())
    
# print(command) # [['push_front', '1'], ['pop_back'], ['front']...]

dq = deque()
for i in range(n):
    
    if len(command[i]) > 1:
        if len(command[i][0]) == 10:  # push_front 일때
            dq.appendleft(int(command[i][1]))
        else:                         # push_back 일때
            dq.append(int(command[i][1]))
        
    else:
        if command[i] == ['pop_front']:
            if len(dq) == 0:
                print(-1)
            else:
                print(dq.popleft())
                
        elif command[i] == ['pop_back']:
            if len(dq) == 0:
                print(-1)
            else:
                print(dq.pop())
                
        elif command[i] == ['size']:
            print(len(dq))
            
        elif command[i] == ['empty']:
            if len(dq) == 0:
                print(1)
            else:
                print(0)
                
        elif command[i] == ['front']:
            if len(dq) != 0:
                print(dq[0])
            else:
                print(-1)
                
        elif command[i] == ['back']:
            if len(dq) != 0:
                print(dq[-1])
            else:
                print(-1)


