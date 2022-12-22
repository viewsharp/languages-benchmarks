import time


def sum_even_numbers_py_1(bottom: int, top: int) -> int:
    return sum(filter(lambda x: x % 2 == 0, range(bottom, top + 1)))


def sum_even_numbers_py_1_1(bottom: int, top: int) -> int:
    return sum(x for x in range(bottom, top + 1) if x % 2 == 0)


def sum_even_numbers_py_2(bottom: int, top: int) -> int:
    result = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result


if __name__ == '__main__':
    start_at = time.process_time()
    res = sum_even_numbers_py_1(2, 20_000_000)
    print(f"sum_even_numbers_py_1: {time.process_time() - start_at}s")
    print(f"sum_even_numbers_py_1: {res}")

    start_at = time.process_time()
    res = sum_even_numbers_py_1_1(2, 20_000_000)
    print(f"sum_even_numbers_py_1_1: {time.process_time() - start_at}s")
    print(f"sum_even_numbers_py_1_1: {res}")

    start_at = time.process_time()
    res = sum_even_numbers_py_2(2, 20_000_000)
    print(f"sum_even_numbers_py_2: {time.process_time() - start_at}s")
    print(f"sum_even_numbers_py_2: {res}")

