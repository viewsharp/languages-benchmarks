run-python:
	docker build --no-cache -t python_benchmark ./python/
	docker run --rm python_benchmark

run-python-numba:
	docker build --no-cache -t python_numba_benchmark ./python_numba/
	docker run --rm python_numba_benchmark

run-cython:
	docker build --no-cache -t cython_benchmark ./cython/
	docker run --rm cython_benchmark

run-pypy:
	docker build --no-cache -t pypy_benchmark ./pypy/
	docker run --rm pypy_benchmark

run-go:
	docker build --no-cache -t go_benchmark ./go/
	docker run --rm go_benchmark

run-rust:
	docker build --no-cache -t rust_benchmark ./rust/
	docker run --rm rust_benchmark

clean:
	docker rmi python_benchmark
	docker rmi python_numba_benchmark
	docker rmi cython_benchmark
	docker rmi pypy_benchmark
	docker rmi go_benchmark
	docker rmi rust_benchmark

all: run-python run-python-numba run-cython run-pypy run-go run-rust  clean