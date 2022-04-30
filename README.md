# Benchmark

Decorator to measure the execution time of a function.

# Install

```
pip install -e .
```

## Example

code eample
``` python3
import benchmark

@benchmark.time
def add(x, y):
    z = x + y
    return z


add(2, 3)
```

result
```
add:0.001[ms]
```
