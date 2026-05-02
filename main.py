from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

```python
# Test qilish
print(fibonacci(10))  # 55
print(fibonacci(20))  # 6765
