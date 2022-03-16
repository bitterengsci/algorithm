
Modern C++ features (after C++11)
- type aliases (using)
- uniform initialization, non-static member initialization
    ```cpp
    class demo {

      public: demo(int var1_, bool var2_, string var3_) : var1(var1_), var2(var2_), var3(var3_) {} 
    };  
    ```
- auto(typed variables are deduced by the compiler according to the type of their initializer)
- range-based for loops      
    ```cpp
    std::array<int, 5> array {1, 2, 3, 4, 5};
    for(int &x : array) { }
    ```
- smart pointers
- nullptr (of type std::nullptr_t and can be implicitly converted into pointer types); NULL is not convertible to integral types except bool
- move semantics
- Variadic templates
- delete, default        demo(const demo &) = delete;  demo &operator=(const demo &) = delete;
- delegating constructors: constructors can call other constructors in the same class using an initializer list
- lambda expression



# Containers in C++ STL (Standard Template Library)
* Sequence Container (can be accessed sequentially)
    - array: Static contiguous array 
    - vector: Dynamic contiguous array 
    - deque: Double-ended queue 
    - forward_list: Singly-linked list 
    - list: Doubly-linked list 
* Associative Container: (sorted data structure, quickly searched in O(logn))
    - Set: Collection of unique keys, sorted by keys
    - Map: Collection of key-value pairs, sorted by keys, keys are unique
    - multiset: Collection of keys, sorted by keys (= set with duplicate keys)
    - multimap: Collection of key-value pairs, sorted by keys 
* Unordered Associatve Container: (unsorted (hashed) data structures, quickly searched O(1) amortized, O(n) worstcase) 
    - unordered_set: Collection of unique keys, hashed by keys
    - unordered_map: Collection of key-value pairs, hashed by keys, keys are unique
    - unordered_multiset: Collection of keys, hashed by keys 
    - unordered_multimap: Collection of key-value pairs, hashed by keys 
* Container Adaptor: a different interface for sequential containers
    - stack: Adapts a container to provide stack (LIFO data structure)
    - queue: Adapts a container to provide queue (FIFO data structure)
    - priority_queue: Adapts a container to provide priority queue



template <typename T>

std::vector<T>
- stores contiguously, elements can be accessed through iterators or using offsets.
- random access O(1)
- insert/remove elements at the end amortized O(1)
- insert/remove elements O(n)


std::tuple<T1, T2...>
- a fixed-size collection of heterogeneous values

std::pair<T1, T2>
- store two heterogeneous objects as a single unit
- a specific case of a std::tuple with two elements

std::queue<T>
- FIFO

std::deque<T>
- indexed sequence container; automatically expanded and contracted
  - Expansion of a deque is cheaper than std::vector because it does not involve copying of the existing elements to a new memory location.
- random access O(1)
- insert/remove elements at the beginning/end O(1)
- insert/remove elements O(n)


std::map<KeyType, ValueType>
- a sorted associative container that contains key-value pairs with unique keys
- implemented as red-black trees
- search/remove/insert O(logn)

std::unordered_map
- an associative container that contains key-value pairs with unique keys
- elements not sorted in any particular order, but organized into buckets (depending on hash of the keys)
- search/remove/insert average O(1)


# Python Aid Sheet
BFS     ->  Queue First In First Out  append, pop(-1)
DFS     ->  Stack Last In First Out   append, pop()
Deque   ->  append (insert element at right end), appendleft (insert element at right end)
            pop (delete element from right end), popleft (delete element from left end)

preorder (node-left-right)
inorder (left-node-right)
postorder (left-right-node)

```python
# % reminder 余数 // divisor 商
dict = dict.keys() = an iterator across dict key

thisdict.update({"key": "value"})
thisdict.pop("key")  # remove the item with the specified key name
del thisdict["key"]
del thisdict # del keyword can also delete the dictionary completely
thisdict.clear()
thisdict.get("key", default_value) 

l = ['c', 'a', 'b']
l.sort(reverse= key=) # no return, modify l inplace
new_l = l.sorted()
new_l = sorted(l)
print(l, new_l) # ['c', 'a', 'b'] ['a', 'b', 'c']

Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort

# argsort without numpy
sorted(range(len(s)), key=lambda k: s[k])
[i for (val, i) in sorted((val, i) for (i, val) in enumerate(seq))]
[x for x, y in sorted(enumerate(seq), key = lambda x: x[1])]
sorted(range(len(seq)), key=seq.__getitem__)

# customize sort (sort in-place, do not return anything)
intervals.sort(key=lambda x: (x[1], -x[0]))

set.add(element)

# zip(*iterables) takes iterables (can be zero or more), aggregates them in a tuple and return it
index = [1, 2]
l = ['c', 'a', 'b']
for i in zip(index, l):
    print(i)
# (1, 'c')
# (2, 'a')

for i, item in enumerate(l):
    print(i, item)
# 0 c
# 1 a
# 2 b

if l1: # if l1 is not None
if not l1: # if l1 is None

for x in 'abcde':  # iterate in string
    print(x)

math.ceil()
math.floor()
round(number, ndigits=2)   # 四舍五入

float('inf')
print(-2**31, 2**31-1)    # -2147483648 2147483647 [-sys.maxsize-1, sys.maxsize]
print(-2**63, 2**63-1)    # [-9223372036854775808, 9223372036854775807] 

R, C = len(matrix), len(matrix[0])
mat = [[0] * C for _ in range(R)] 

range(len(T) - 1, -1, -1) = reversed(range(T))   # reversely

# binary search
start, end = 0, len(nums) - 1
while start + 1 < end:
    mid = start + (end - start) // 2   # mid = (start + end) // 2 no overflow  or >> 1
    if CONDITION:
        end = mid
    else:
        start = mid
```