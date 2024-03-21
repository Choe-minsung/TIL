import sys
input = sys.stdin.readline


hour, min = map(int, input().split())

if min < 45:
    if hour != 0:
        hour -= 1
        min += 15
    
    else:
        hour = 23
        min += 15
else:
    min -= 45
    
print(hour, min)