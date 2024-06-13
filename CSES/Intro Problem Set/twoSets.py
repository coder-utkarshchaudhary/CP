x = int(input())

total_sum = x * (x + 1) // 2

# Check if the total sum is even
if total_sum % 2 != 0:
    print("NO")
else:
    half_sum = total_sum // 2
    current_sum = 0
    left, right = [], []
    
    for i in range(1, x + 1):
        if current_sum + i <= half_sum:
            left.append(i)
            current_sum += i
        else:
            right.append(i)
    
    print("YES")
    print(len(left))
    for left_num in left:
        print(left_num, end=" ")
    print()
    print(len(right))
    for right_num in right:
        print(right_num, end=" ")
