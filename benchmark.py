from contextlib import contextmanager
from functools import partial
from threading import Thread
from time import time
from typing import Callable, Generator

from gil_free_python import gil_freed_fibonacci, not_gil_freed_fibonacci

from compiled_py import fibonacci as nuitka_fibonacci
from fibonacci import fibonacci


@contextmanager
def timer() -> Generator[None, None, None]:
    t = time()
    yield
    print(f"Time spent: {time() - t}")


def run_in_thread(func: Callable[[], int], *, thread_count: int) -> None:
    threads: list[Thread] = []
    for i in range(thread_count):
        t = CustomizedThread(func, name=f"Thread {i:1d}")
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


class CustomizedThread(Thread):
    def __init__(self, func: Callable[[], int], *, name: str) -> None:
        self._func = func
        self._tname = name
        super().__init__(daemon=True)

    def run(self) -> None:
        res = self._func()
        print(f"{self._tname} done: {res}")


N = 40

print("--- Pure Python ---")
with timer():
    res = fibonacci(N)
    print(f"Result: {res}")

print("--- Compiled Python ---")
with timer():
    res = nuitka_fibonacci(N)
    print(f"Result: {res}")

print("--- Rust Binding not GIL freed ---")
with timer():
    res = not_gil_freed_fibonacci(N)
    print(f"Result: {res}")

print("--- Rust Binding GIL freed ---")
with timer():
    res = gil_freed_fibonacci(N)
    print(f"Result: {res}")


# python thread
print("--- Python thread ---")
with timer():
    run_in_thread(partial(fibonacci, N), thread_count=10)

# python thread
print("--- Compiled Python thread ---")
with timer():
    run_in_thread(partial(nuitka_fibonacci, N), thread_count=10)

# gil freed thread
print("--- Not GIL freed thread ---")
with timer():
    run_in_thread(partial(not_gil_freed_fibonacci, N), thread_count=10)

# gil freed thread
print("--- GIL freed thread ---")
with timer():
    run_in_thread(partial(gil_freed_fibonacci, N), thread_count=10)
