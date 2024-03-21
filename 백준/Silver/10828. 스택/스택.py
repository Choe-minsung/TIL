# 백준 : 10828 스택

# 정수저장 스택 구현

# push X: 정수 X를 스택에 넣기
# pop: 스택에서 가장 위에 있는 정수를 빼고 그 수를 출력. 스택에 들어있는 정수가 없는 경우에는 -1을 출력.
# size: 스택에 들어있는 정수의 개수를 출력.
# empty: 스택가 비어있으면 1, 아니면 0을 출력.
# top: 스택의 가장 위에 있는 정수를 출력. 스택에 들어있는 정수가 없는 경우에는 -1을 출력.

import sys
input = sys.stdin.readline

n = int(input())

command = []
for i in range(n):
    command.append(input().split())
    
# print(command) # [['push', '1'], ['front']...]

val = []
for i in range(n):
    
    if len(command[i]) > 1:
        val.append(int(command[i][1]))
        
    else:
        if command[i] == ['pop']:
            if len(val) == 0:
                print(-1)
            else:
                print(val.pop())
                
        elif command[i] == ['size']:
            print(len(val))
            
        elif command[i] == ['empty']:
            if len(val) == 0:
                print(1)
            else:
                print(0)
                
        elif command[i] == ['top']:
            if len(val) != 0:
                print(val[-1])
            else:
                print(-1)