def count_triplets(t, test_cases):
    results = []
    for n, x in test_cases:
        count = 0
        for a in range(1, x + 1):
            for b in range(1, x - a + 1):
                max_c_by_sum = x - a - b
                if a + b > n:
                    continue
                max_c_by_product = (n - a * b) // (a + b)
                max_c = min(max_c_by_sum, max_c_by_product)
                if max_c > 0:
                    count += max_c
        results.append(count)
    return results

# Read input
t = int(input().strip())
test_cases = [tuple(map(int, input().strip().split())) for _ in range(t)]

# Get results
results = count_triplets(t, test_cases)

# Print results
for result in results:
    print(result)