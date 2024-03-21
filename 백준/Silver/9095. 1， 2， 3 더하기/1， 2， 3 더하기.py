val = [0] * 11

val[0] = 0 # n = 0 일때 경우의 수
val[1] = 1 # n = 1 일때 경우의 수 / 1
val[2] = 2 # n = 2 일때 경우의 수 / 1+1, 2
val[3] = 4 # n = 3 일때 경우의 수 / 1+1+1, 1+2, 2+1, 3

for i in range(1,8):
    val[i+3] = val[i] + val[i+1] + val[i+2] # val[1] + val[2] + val[3] -> val[4]
    
n = int(input())

for i in range(n):
    print(val[int(input())])