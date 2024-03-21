# 백준 20300 : 서강근육맨

# n개의 운동기구
# 2개까지 sum 가능

n = int(input())
temp = list(map(int, input().split()))

temp.sort()

m = 0

if n % 2 == 1:  # n 이 홀수일때 최대값 pop
    m = temp.pop()

for i in range(int(len(temp) / 2)):  
    m = max(m, (temp[i] + temp[-i-1]))  # 정렬 후 앞,뒤요소 1개씩 가져와 max값 저장
               
print(m)