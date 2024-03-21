total = int(input()) # case 수

k = []
n = []

val = []

for i in range(total):
    
    result = list(range(1,15)) # 0층 사람수 (문제조건 중, 1 <= k, n <= 14)
    
    k.append(int(input())) # 층
    n.append(int(input())) # 호
    
    for j in range(k[i]): # 0층 ~ k-1층
        for q in range(1, n[i]): # 1호 ~ n-1호
            result[q] = result[q] + result[q-1] # 각 j 층별 1,2,3... n호까지 / q호 = q호 + (q-1)호
    val.append(result[n[i]-1])
    
for t in range(total):
    print(val[t])