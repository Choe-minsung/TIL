# 백준 : 1068 트리

# 리프노드 : 자식이 없는 마지막 노드
# 노드 삭제시, 그 노드의 모든 자손도 삭제

import sys
input = sys.stdin.readline

n = int(input())

graph = list(map(int, input().split())) # 0번노드 ~ n-1번 노드의 각각 부모번호 저장, 부모 없으면 -1

removal = int(input()) # 지울 노드 번호


# case 1) 삭제처리를 False로 받기 : 0도 False이므로 겹침!

# def dfs(v): # dfs 함수 정의
#     graph[v] = False # 삭제처리(방문처리)
    
#     for i in range(n):
#         if v == graph[i]: # v가 i의 부모인 경우, i도 삭제처리 
#             dfs(i)

# case 2) 삭제처리를 임의의 수(-100)로 받기 : sol! 
        
def dfs(v): # dfs 함수 정의
    graph[v] = -100 # 삭제처리(방문처리)
    
    for i in range(n):
        if v == graph[i]: # v가 i의 부모인 경우, i도 삭제처리 
            dfs(i)
            
            
dfs(removal)

cnt = 0
for i in range(n): 
    
    if graph[i] != -100: # i가 삭제처리 되지 않은 경우
        
        if i not in graph: # i 가 부모노드가 아닌 경우 (리프노드인 경우)
            cnt += 1

print(cnt)