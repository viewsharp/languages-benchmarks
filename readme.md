# Python
Python: 3.11.1 (main, Jan 23 2023, 21:04:06) [GCC 10.2.1 20210110]  
Test case: sum_even_numbers(2, 20_000_000)  

```python
def sum_even_numbers_1(bottom: int, top: int) -> int:
    return sum(filter(lambda x: x % 2 == 0, range(bottom, top + 1)))
```
Repeats: 3  
Best execution time: 1198ms  

```python
def sum_even_numbers_2(bottom: int, top: int) -> int:
    return sum(x for x in range(bottom, top + 1) if x % 2 == 0)
```
Repeats: 3  
Best execution time: 1102ms  

```python
def sum_even_numbers_3(bottom: int, top: int) -> int:
    result = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result
```
Repeats: 3  
Best execution time: 1108ms  

# Python + numba
Python: 3.10.9 (main, Jan 23 2023, 22:32:48) [GCC 10.2.1 20210110]  
Numba: 0.56.4  
Test case: sum_even_numbers(2, 20_000_000)  

```python
@numba.njit()
def sum_even_numbers(bottom: int, top: int) -> int:
    result = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result
```
Repeats: 100  
Best execution time: 6.6ms  

# Cython
Python: 3.11.1 (main, Jan 23 2023, 21:04:06) [GCC 10.2.1 20210110]  
Cython: 0.29.33  
Test case: sum_even_numbers(2, 20_000_000)  

```python
def sum_even_numbers_1(bottom: int, top: int) -> int:
    return sum(filter(lambda x: x % 2 == 0, range(bottom, top + 1)))
```
Repeats: 5  
Best execution time: 707ms  

```python
def sum_even_numbers_1_1(bottom: int, top: int) -> int:
    return sum(x for x in range(bottom, top + 1) if x % 2 == 0)
```
Repeats: 5  
Best execution time: 518ms  

```python
def sum_even_numbers_2(bottom: int, top: int) -> int:
    result = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result
```
Repeats: 5  
Best execution time: 470ms  

```python
def sum_even_numbers_2_1(bottom: int, top: int) -> int:
    cdef long long result = 0
    cdef long long x = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result
```
Repeats: 100  
Best execution time: 26ms

# PyPy
Pypy: 3.7.13 (7e0ae751533460d5f89f3ac48ce366d8642d1db5, Mar 29 2022, 06:03:31)
[PyPy 7.3.9 with GCC 10.2.1 20210130 (Red Hat 10.2.1-11)]  
Test case: sum_even_numbers(2, 20_000_000)  

```python
def sum_even_numbers_1(bottom: int, top: int) -> int:
    return sum(filter(lambda x: x % 2 == 0, range(bottom, top + 1)))
```
Repeats: 1  
Best execution time: 3745ms  

```python
def sum_even_numbers_2(bottom: int, top: int) -> int:
    return sum(x for x in range(bottom, top + 1) if x % 2 == 0)
```
Repeats: 10  
Best execution time: 394ms  

```python
def sum_even_numbers_3(bottom: int, top: int) -> int:
    result = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result
```
Repeats: 100  
Best execution time: 28ms 

# Go
Go: go1.19.2  
Test case: sumEvenNumbers(2, 20_000_000)  

```go
func sumEvenNumbers(bottom int64, top int64) int64 {
    var result int64 = 0
    for x := bottom; x < top+1; x++ {
        if x%2 == 0 {
            result += x
        }
    }
    return result
}
```
Repeats: 100  
Best execution time: 5.2687ms

# Rust
Test case: sum_even_numbers(2, 20_000_000)  

```rust
fn sum_even_numbers(bottom: i64, top: i64) -> i64 {
    return (bottom..=top).filter(|x| x % 2 == 0).sum()
}
```
Repeats: 100  
Best execution time: 3.99ms  
