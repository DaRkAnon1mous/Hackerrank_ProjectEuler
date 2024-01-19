#!/bin/python3

def get_grid():
    grid = []
    for _ in range(20):
        row = list(map(int, input().split()))
        grid.append(row)
    return grid

def greatest_product(grid):
    max_product = 0

    # Check horizontally
    for i in range(20):
        for j in range(17):
            product = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
            max_product = max(max_product, product)

    # Check vertically
    for i in range(17):
        for j in range(20):
            product = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
            max_product = max(max_product, product)

    # Check diagonally (left to right)
    for i in range(17):
        for j in range(17):
            product = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
            max_product = max(max_product, product)

    # Check diagonally (right to left)
    for i in range(17):
        for j in range(3, 20):
            product = grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3]
            max_product = max(max_product, product)

    return max_product

if __name__ == "__main__":
    grid = get_grid()
    result = greatest_product(grid)
    print(result)
