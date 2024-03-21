# 백준 : 2212 센서

# n 개 센서, k 개 집중국
# 각 n이 적어도 하나의 k 연결
# 수신영역 길이의 합 최소
# k개의 그룹으로 나누어 그룹 별 max - min 의 합의 최솟값

n = int(input())
k = int(input())

temp = list(map(int, input().split()))

temp.sort()

# print(temp)
# [1, 3, 6, 6, 7, 9] -> (1, 3) + (6, 7, 9) : (3 - 1) = 2 + (9 - 6) = 3 -> 5
# 1, 3 / 6, 6, 7, 9 -> (1, 3) + (6, 6, 7, 9) : (3 - 1) = 2 + (9 - 6) = 3 -> 5

val = []
for i in range(n-1):
    val.append(temp[i+1] - temp[i]) # 각 센서 간 간격

val.sort()

# print(val) # [0, 1, 2, 2, 3]


# 간격이 긴 곳을 기준으로 나누어 집중국 배치 -> val의 맨 뒤값 k개 만큼 빼고 나머지 sum

if k != 1:
    answer = sum(val[:-k+1])
    print(answer)
    
else:
    answer = sum(val)
    print(answer)
