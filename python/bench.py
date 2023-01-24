import timeit
import sys
import inspect


def sum_even_numbers_1(bottom: int, top: int) -> int:
    return sum(filter(lambda x: x % 2 == 0, range(bottom, top + 1)))


def sum_even_numbers_2(bottom: int, top: int) -> int:
    return sum(x for x in range(bottom, top + 1) if x % 2 == 0)


def sum_even_numbers_3(bottom: int, top: int) -> int:
    result = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result


if __name__ == '__main__':
    function_call = 'sum_even_numbers(2, 20_000_000)'
    functions = [
        (sum_even_numbers_1, 3),
        (sum_even_numbers_2, 3),
        (sum_even_numbers_3, 3),
    ]

    print(f'Python: {sys.version}  ')
    print(f'Test case: {function_call}  ')
    print()

    for func, repeats in functions:
        sum_even_numbers = func
        best_execution_time = min(timeit.repeat(function_call, globals=locals(), repeat=repeats, number=1))

        print('```python')
        print(inspect.getsource(func).strip('\n'))
        print('```')
        print(f'Repeats: {repeats}  ')
        print(f'Best execution time: {best_execution_time * 1000:0.0f}ms  ')
        print()
