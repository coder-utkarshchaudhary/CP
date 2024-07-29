num_test_cases = int(input())
ans = []

for _ in range(num_test_cases):
    n = int(input())
    _min = float('inf')
    
    for y in range(n//4+1):
        _min = min(_min, y+(n//2-2*y))
    
    ans.append(_min)

for num in ans:
    print(num)