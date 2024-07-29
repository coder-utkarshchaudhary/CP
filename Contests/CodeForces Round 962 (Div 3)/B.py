num_test_cases = int(input())

results = []

for _ in range(num_test_cases):
    grid_size, reduction_factor = map(int, input().split())
    grid = []

    for i in range(grid_size):
        grid.append(input().strip())

    if reduction_factor == 1:
        results.append(grid)
        continue

    reduced_grid_size = grid_size // reduction_factor
    reduced_grid = []

    for row_block in range(reduced_grid_size):
        new_row = []
        for col_block in range(reduced_grid_size):
            cell_value = grid[row_block * reduction_factor][col_block * reduction_factor]
            new_row.append(cell_value)
        reduced_grid.append(new_row)

    results.append(reduced_grid)

for result in results:
    for row in result:
        print("".join(row))