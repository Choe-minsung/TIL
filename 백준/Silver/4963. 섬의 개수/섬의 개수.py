# 백준 4963 : 섬의개수

# 지도 : 가로(w) x 세로(h)
# 0 : 바다, 1 : 땅 / 가로,세로,대각선에 붙어있으면 1개 취급

from collections import deque

# 가로(왼, 오), 세로(위, 아래), 대각선(왼위, 오위, 왼아래, 오아래)
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def bfs(x, y):
    q = deque([[x,y]])
    graph[y][x] = 0 # 방문처리 -> 0 (바다취급) / * x : 가로, y : 세로 * 
    
    while q:
        x, y = q.popleft() # q 왼쪽 pop
        
        for i in range(8):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < w) & (0 <= ny < h):
                if graph[ny][nx] == 1: # 미방문일때 (1 : 땅)
                    q.append([nx, ny])
                    graph[ny][nx] = 0 # 방문처리

          
while(True):
    w, h = map(int, input().split()) # w : 가로, h : 세로
    
    if (w == 0) & (h == 0): # 종료조건
        break
        
    cnt = 0
    graph = []
    
    for i in range(h):
        graph.append(list(map(int, input().split())))
        
    for i in range(w): 
        for j in range(h):
            if graph[j][i] == 1: # * x : 가로, y : 세로 * 
                bfs(i, j) 
                cnt += 1 # 섬의 묶음 count + 1
                
    print(cnt)