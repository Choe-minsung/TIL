# 백준 : 1874 스택 수열

# 스택 : LIFO(후입선출)
# push : +, pop : -

import sys
input = sys.stdin.readline

n = int(input())

nums = []  # target stack

for i in range(n):
    nums.append(int(input()))

# nums  # [4, 3, 6, 8, 7, 5, 2, 1]

temp = []
answer = []
flag = 1

for i in range(n):
    
    while(flag <= nums[i]):  # flag가 nums[i] 보다 작거나 같으면, nums[i]까지 flag + 1 하면서 stack
        temp.append(flag)
        answer.append('+')
        flag += 1
        
    if temp[-1] == nums[i]: # 맨 뒤에 target이 있으면 pop
        temp.pop()
        answer.append('-')
    else:
        answer = 'NO'  # 맨 뒤에 target이 아니면 break
        break
    
if answer == 'NO':
    print(answer)
else:
    for i in range(len(answer)):
        print(answer[i])