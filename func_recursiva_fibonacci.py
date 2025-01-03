from functools import lru_cache


@lru_cache
def fibonacci_sequence(n: int) -> int:
    """Sequência Fibonacci with memoization"""
    if n < 1:
        return 0
    if n <= 2:
        return 1
    return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)


if __name__ == "__main__":
    for i in range(10):
        print(fibonacci_sequence(i))