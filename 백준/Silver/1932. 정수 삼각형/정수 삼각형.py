import sys
input = sys.stdin.readline

n = int(input())

val = []
for i in range(n):
    val.append(list(map(int, input().split())))
    
# print(val) # [ [1], [1,2], [1,2,3] ]



for i in range(1, n): # i : 2 ~ (n-1)
    for j in range(i+1): # j : 0 ~ i
        
        if j == 0:
            val[i][j] += val[i-1][j] # 맨 왼쪽 값 합산
            
        elif j == i:
            val[i][j] += val[i-1][j-1] # 맨 오른쪽 값 합산
            
        else:
            val[i][j] += max(val[i-1][j-1], val[i-1][j]) # 직전 i 층, j-1 or j 값들중 max값으로 합산
    
    
# print(val) # [ [1], [2,2], [3,4,3] ]

print(max(val[n-1]))