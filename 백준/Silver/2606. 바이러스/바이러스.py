from collections import deque

N = int(input()) # node 수
M = int(input()) # 간선 수

graph = [ [False] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (N + 1)    


def bfs(V):
    global cnt
    cnt = -1
    
    q = deque([V])
    visited[V] = True
    
    while q:
        V = q.popleft()
#         print(str(V) + '번 node를 방문합니다.')
        cnt += 1 # node 방문 시 마다 cnt+1
        
        for i in range(1, N+1):
            if not visited[i] and graph[V][i]:
                q.append(i)
                visited[i] = True
                
bfs(1)
print(cnt)