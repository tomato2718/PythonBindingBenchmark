# Python BindingBenchmark

Testing performance of different ways to optimize Python modules under multithreaded environments.

## Environment

Testing under:

- MacBook Pro 2023 (Apple M2 Pro)
- Python 3.12.10
- Rust 1.85.1

## Code

Running fibonacci recursively without cache to simulate CPU bound tasks.

See: `benchmark.py`

## Result

Time spent for each approach (seconds)

|               | Pure Python | Nuitka Compiled python | Rust PyO3 | Rust PyO3 GIL freed |
|---------------|-------------|------------------------|-----------|---------------------|
| Single thread | 8.532176    | 5.653137               | 0.660262  | 0.649581            |
| 10 threads    | 86.446902   | 56.112609              | 6.600356  | 1.041696            |

## Output

```sh
--- Pure Python ---
Result: 102334155
Time spent: 8.53217601776123
--- Compiled Python ---
Result: 102334155
Time spent: 5.65313720703125
--- Rust Binding not GIL freed ---
Result: 102334155
Time spent: 0.6602621078491211
--- Rust Binding GIL freed ---
Result: 102334155
Time spent: 0.6495819091796875
--- Python thread ---
Thread 0 done: 102334155
Thread 6 done: 102334155
Thread 9 done: 102334155
Thread 1 done: 102334155
Thread 2 done: 102334155
Thread 5 done: 102334155
Thread 3 done: 102334155
Thread 4 done: 102334155
Thread 7 done: 102334155
Thread 8 done: 102334155
Time spent: 86.44690299034119
--- Compiled Python thread ---
Thread 0 done: 102334155
Thread 1 done: 102334155
Thread 2 done: 102334155
Thread 3 done: 102334155
Thread 4 done: 102334155
Thread 5 done: 102334155
Thread 7 done: 102334155
Thread 6 done: 102334155
Thread 8 done: 102334155
Thread 9 done: 102334155
Time spent: 56.11260986328125
--- Not GIL freed thread ---
Thread 0 done: 102334155
Thread 1 done: 102334155
Thread 2 done: 102334155
Thread 3 done: 102334155
Thread 4 done: 102334155
Thread 5 done: 102334155
Thread 6 done: 102334155
Thread 7 done: 102334155
Thread 8 done: 102334155
Thread 9 done: 102334155
Time spent: 6.600356101989746
--- GIL freed thread ---
Thread 4 done: 102334155
Thread 9 done: 102334155
Thread 2 done: 102334155
Thread 7 done: 102334155
Thread 0 done: 102334155
Thread 1 done: 102334155
Thread 3 done: 102334155
Thread 5 done: 102334155
Thread 6 done: 102334155
Thread 8 done: 102334155
Time spent: 1.0416960716247559
```