def t(n):
    tri = [1,1,1,2,2,3,4,5]
    
    for i in range(8, n):
        tri.append(tri[i-1] + tri[i-5])
        
    return tri[n-1]


n = int(input())

for i in range(n):
    print(t(int(input())))