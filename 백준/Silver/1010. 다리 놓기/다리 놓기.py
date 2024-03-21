def f(n):
    fac = [1]
    
    for i in range(n):
        fac.append(fac[i] * (i+1))

    return fac[n]

n = int(input())

val = []
for i in range(n):
    val.append(list(map(int, input().split())))
    
for i in range(n):
    b = val[i][1]
    a = val[i][0]
    print(int(f(b) / (f(b-a) * f(a))))