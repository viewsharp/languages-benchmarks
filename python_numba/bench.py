import timeit
import sys
import inspect

import numba


@numba.njit()
def sum_even_numbers(bottom: int, top: int) -> int:
    result = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result


if __name__ == '__main__':
    function_call = 'sum_even_numbers(2, 20_000_000)'
    repeats = 100

    best_execution_time = min(timeit.repeat(function_call, globals=locals(), repeat=repeats, number=1))

    print(f'Python: {sys.version}  ')
    print(f'Numba: {numba.__version__}  ')
    print(f'Test case: {function_call}  ')
    print()
    print('```python')
    print(inspect.getsource(sum_even_numbers).strip('\n'))
    print('```')
    print(f'Repeats: {repeats}  ')
    print(f'Best execution time: {best_execution_time * 1000:0.1f}ms  ')
