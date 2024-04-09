import sys
input = sys.stdin.readline

# N개 숫자카드
# N개 중 M개 수를 각각 갖고있는지 여부 (1 or 0)

def sol():
    n = int(input())
    
    n_list = sorted(list(map(int, input().split()))) # sorted()로 받을 때 한번에 정렬
    
    m = int(input())
    
    m_list = list(map(int, input().split())) # 10 9 -5 2 3 4 5 -10

#     answer = [0 for i in range(m)] # answer 리스트 받아놓기 -> 비효율적, loop에 바로 print(end = ' ') 하기
    
    n_list.sort()
    
    
    for num in m_list:
        
        start = 0 # n_list 탐색 시작 범위
        end = n-1 # n_list 탐색 끝 범위
        temp = False # print 할 answer / 0 or 1 출력은 간단히 boolean으로 지정하기!
        
        while(start <= end):
            mid = (start + end) // 2
            
            if n_list[mid] < num:
                start = mid + 1
                
            elif n_list[mid] > num:
                end = mid - 1
                
            else:
                temp = True
                break
            
        print(1 if temp else 0, end = ' ') # list comprehension / boolean 조건문으로 간단히 0 or 1 출력 / end 구문으로 공백
    
    



sol()
