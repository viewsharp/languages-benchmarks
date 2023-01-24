import timeit
import sys

import Cython

from bench_ext import sum_even_numbers_1, sum_even_numbers_1_1, sum_even_numbers_2, sum_even_numbers_2_1

sum_even_numbers_1_code = """
def sum_even_numbers_1(bottom: int, top: int) -> int:
    return sum(filter(lambda x: x % 2 == 0, range(bottom, top + 1)))
"""

sum_even_numbers_1_1_code = """
def sum_even_numbers_1_1(bottom: int, top: int) -> int:
    return sum(x for x in range(bottom, top + 1) if x % 2 == 0)
"""

sum_even_numbers_2_code = """
def sum_even_numbers_2(bottom: int, top: int) -> int:
    result = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result
"""

sum_even_numbers_2_1_code = """
def sum_even_numbers_2_1(bottom: int, top: int) -> int:
    cdef long long result = 0
    cdef long long x = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result
"""


if __name__ == '__main__':
    function_call = 'sum_even_numbers(2, 20_000_000)'
    functions = [
        (sum_even_numbers_1, sum_even_numbers_1_code, 5),
        (sum_even_numbers_1_1, sum_even_numbers_1_1_code, 5),
        (sum_even_numbers_2, sum_even_numbers_2_code, 5),
        (sum_even_numbers_2_1, sum_even_numbers_2_1_code, 100),
    ]

    print(f'Python: {sys.version}  ')
    print(f'Cython: {Cython.__version__}  ')
    print(f'Test case: {function_call}  ')
    print()

    for func, code, repeats in functions:
        sum_even_numbers = func
        best_execution_time = min(timeit.repeat(function_call, globals=locals(), repeat=repeats, number=1))

        print('```python')
        print(code.strip('\n'))
        print('```')
        print(f'Repeats: {repeats}  ')
        print(f'Best execution time: {best_execution_time * 1000:0.0f}ms  ')
        print()

