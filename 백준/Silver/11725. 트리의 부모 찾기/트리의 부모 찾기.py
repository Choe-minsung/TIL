# 백준 11725 : 트리의 부모찾기

# 각 노드의 부모?

import sys
input = sys.stdin.readline

from collections import deque


def bfs(v):
    q = deque([v])
    visited[v] = True
    
    while q:
        v = q.popleft()
        
        for n in graph[v]:
            if not visited[n]:
                visited[n] = True # 방문처리
                answer[n] = v 
                q.append(n)
                




n = int(input()) # 노드개수

graph = [ [False] for _ in range(n + 1) ] # n x 1 행렬 / graph.append() 방식으로 노드번호 추가
visited = [False] * (n + 1)
answer = [False] * (n + 1)

for i in range(n-1): # 시작노드 제외한 range 설정
    a, b = map(int, input().split())
    graph[a].append(b) 
    graph[b].append(a) # a, b는 양방향 연결


bfs(1) # 문제조건) 시작노드 : 1


for i in range(2, n + 1): # 2번 노드부터, 각 노드의 부모노드번호 
        print(answer[i])   





