x = int(input())
nums = list(map(int, input().split()))[:x]

moves = 0

for i in range(x-1):
    if nums[i] > nums[i+1]:
        moves = moves+(nums[i]-nums[i+1])
        nums[i+1] = nums[i]
    else:
        pass

print(moves)