from examples import sudoku_9x9, sudoku_4x4
from sudoku import solve_sudoku


def solve(field, dimension):
    for i, res in enumerate(solve_sudoku(field, dimension)):
        print(f'Solution {i + 1}:')
        for x in range(dimension):
            print(*res[x])
        print()


if __name__ == '__main__':
    solve(sudoku_4x4, 4)
    solve(sudoku_9x9, 9)
