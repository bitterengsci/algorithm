

# Binary Search



# BFS & DFS


# Monotonous Stack
```python
class MonoStack():
    def __init__(self):
        self.stack() = []

    def pop(self):
        return self.stack.pop()

    # 新元素插入前, pop掉所有比它大的
    def append(self, a):
        self.push(a)

    def push(self, a, strict=False):
        i = len(self.stack) - 1
        while i >= 0:
            if self.stack[i] > a:
                self.stack.pop()
            elif self.stack[i] == a and strict:
                self.stack.pop()
            else:
                break
        self.stack.append(a)
```