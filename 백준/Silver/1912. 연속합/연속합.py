n = int(input())

nums = list(map(int, input().split()))

for i in range(1, n): # i : 1 ~ (n-1)
    if nums[n-i-1] <= nums[n-i] + nums[n-i-1]:
        nums[n-i-1] = nums[n-i] + nums[n-i-1]        

print(max(nums))