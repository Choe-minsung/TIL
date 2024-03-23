# 백준 : 수 찾기 1920

import sys
input = sys.stdin.readline

def sol():
    n = int(input())
    
    arr_n = list(map(int, input().split()))
    
    m = int(input())
    
    arr_m = list(map(int, input().split()))
    
    arr_n.sort()
    

    for num in arr_m:
        
        start = 0
        end = n - 1
        
        check = False  # 일치하는 수 체크 변수
        

        while(start <= end):

            mid = (start + end) // 2  # 정렬 돤 arr_n 의 중간 idx 값

            if num == arr_n[mid]:   # 일치 case
                check = True
                print(1)
                break
            
            elif num > arr_n[mid]:
                start = mid + 1

            else:
                end = mid - 1

                
        if not check: # 일치하지 않을 때
            print(0)



sol()




