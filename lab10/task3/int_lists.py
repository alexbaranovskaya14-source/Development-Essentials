from random import randint, seed

seed(42)

a: list[int] = [randint(1, 100) for _ in range(10)]
b: list[int] = [randint(1, 100) for _ in range(10)]
c: list[int] = [randint(1, 100) for _ in range(10)]
d: list[int] = [randint(1, 100) for _ in range(10)]
