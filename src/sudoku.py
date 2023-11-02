import math


def possible_values(field, x, y, dim):
    result = set([i + 1 for i in range(dim)])
    box = math.isqrt(dim)
    for i in range(dim):
        result -= {field[x][i], field[i][y]}
    result -= set([field[x // box * box + xs][y // box * box + ys] for xs in range(box) for ys in range(box)])
    return result


def solve_sudoku(field, dim, pos=0):
    x, y = pos // dim, pos % dim
    if pos >= dim ** 2:
        yield field
    elif field[x][y] != 0:
        yield from solve_sudoku(field, dim, pos + 1)
    else:
        for v in possible_values(field, x, y, dim):
            field[x][y] = v
            yield from solve_sudoku(field, dim, pos + 1)
            field[x][y] = 0
