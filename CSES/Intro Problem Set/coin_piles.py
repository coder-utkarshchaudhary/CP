num_test_cases = int(input())
test_cases = []

for _ in range(num_test_cases):
    test_cases.append(map(int, input().split()))

for left_pile, right_pile in test_cases:
    if left_pile == 0 and right_pile == 0:
        print("YES")
        continue

    if left_pile == 0 or right_pile == 0:
        print("NO")
        continue

    if (left_pile+right_pile)%3 == 0:
        print("YES")
    else:
        print("NO")