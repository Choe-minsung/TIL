# 백준 : 10845 큐

# 정수저장 큐 생성

# push X: 정수 X를 큐에 넣기
# pop: 큐에서 가장 앞에 있는 정수를 빼고 그 수를 출력. 큐에 들어있는 정수가 없는 경우에는 -1을 출력.
# size: 큐에 들어있는 정수의 개수를 출력.
# empty: 큐가 비어있으면 1, 아니면 0을 출력.
# front: 큐의 가장 앞에 있는 정수를 출력. 큐에 들어있는 정수가 없는 경우에는 -1을 출력.
# back: 큐의 가장 뒤에 있는 정수를 출력. 큐에 들어있는 정수가 없는 경우에는 -1을 출력.

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
                print(val.pop(0))
                
        elif command[i] == ['size']:
            print(len(val))
            
        elif command[i] == ['empty']:
            if len(val) == 0:
                print(1)
            else:
                print(0)
                
        elif command[i] == ['front']:
            if len(val) != 0:
                print(val[0])
            else:
                print(-1)
                
        elif command[i] == ['back']:
            if len(val) != 0:
                print(val[-1])
            else:
                print(-1)