def sum_even_numbers_1(bottom: int, top: int) -> int:
    return sum(filter(lambda x: x % 2 == 0, range(bottom, top + 1)))

def sum_even_numbers_1_1(bottom: int, top: int) -> int:
    return sum(x for x in range(bottom, top + 1) if x % 2 == 0)

def sum_even_numbers_2(bottom: int, top: int) -> int:
    result = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result

def sum_even_numbers_2_1(bottom: int, top: int) -> int:
    cdef long long result = 0
    cdef long long x = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result
