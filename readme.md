# Python
##### Version
- Python 3.11.0 (main, Oct 25 2022, 14:13:24) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin

##### Benchmark code
```python
start_at = time.time()
res = sum_even_numbers(2, 20_000_000)
print(time.time() - start_at)
```

##### Variance 1. Execution time: 1640ms
```cython
def sum_even_numbers(bottom: int, top: int) -> int:
    return sum(filter(lambda x: x % 2 == 0, range(bottom, top + 1)))
```

##### Variance 2. Execution time: 1160ms
```cython
def sum_even_numbers(bottom: int, top: int) -> int:
    result = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result
```

# PyPy
##### Version
- Python 3.7.13 (7e0a, Apr 26 2022, 09:29:08) [PyPy 7.3.9 with GCC Apple LLVM 13.1.6 (clang-1316.0.21.2)] on darwin
##### Benchmark code
```python
start_at = time.time()
res = sum_even_numbers(2, 20_000_000)
print(time.time() - start_at)
```

##### Variance 1. Execution time: 3815ms
```cython
def sum_even_numbers(bottom: int, top: int) -> int:
    return sum(filter(lambda x: x % 2 == 0, range(bottom, top + 1)))
```

##### Variance 2. Execution time: 41.9ms
```cython
def sum_even_numbers(bottom: int, top: int) -> int:
    result = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result
```

# Cython
##### Version
- Python 3.11.0 (main, Oct 25 2022, 14:13:24) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
- Cython 0.29.32

##### Benchmark code
```python
start_at = time.time()
res = sum_even_numbers_cy(2, 20_000_000)
print(time.time() - start_at)
```

##### Variance 1. Execution time: 906ms
```cython
def sum_even_numbers_cy(bottom: int, top: int) -> int:
    return sum(filter(lambda x: x % 2 == 0, range(bottom, top + 1)))
```

##### Variance 2. Execution time: 614ms
```cython
def sum_even_numbers_cy(bottom: int, top: int) -> int:
    result = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result
```

##### Variance 3. Execution time: 25.0ms
```cython
def sum_even_numbers_cy(bottom: int, top: int) -> int:
    cdef long long result = 0
    cdef long long x = 0
    for x in range(bottom, top + 1):
        if x % 2 == 0:
            result += x
    return result
```

# Go
##### Version
- Go 1.19.3 darwin/amd64

##### Benchmark code
```go
func main() {
	startAt := time.Now()
	res := sumEvenNumbers(2, 20_000_000)
	fmt.Println(time.Now().Sub(startAt), res)
}
```

##### Variance 1. Execution time: 14.1ms
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

# Rust
##### Version
- Rustc 1.61.0 (fe5b13d68 2022-05-18)

##### Benchmark code
```rust
fn main() {
    let start_at = Instant::now();
    let res = sum_even_numbers(2, 20_000_000);
    println!("{:.2?}", start_at.elapsed());
    println!("{}", res)
}
```

##### Variance 1. Execution time: 7.37ms
```rust
fn sum_even_numbers(bottom: i64, top: i64) -> i64 {
    return (bottom..=top).filter(|x| x % 2 == 0).sum()
}
```
