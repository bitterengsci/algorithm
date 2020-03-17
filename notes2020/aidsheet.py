
% reminder 余数 // divisor 商
dict.keys() -> list

l = ['c', 'a', 'b']
l.sort(reverse= key=) # no return, modify l inplace
new_l = l.sorted()
new_l = sorted(l)
print(l, new_l) # ['c', 'a', 'b'] ['a', 'b', 'c']
# Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort

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

print(-2**31, 2**31-1)    # -2147483648 2147483647 [-sys.maxsize-1, sys.maxsize]
print(-2**63, 2**63-1)    # [-9223372036854775808, 9223372036854775807] 

BFS -> Queue First In First Out  append, pop(-1)
DFS -> Stack Last In First Out   append, pop()
Deque -> append (insert element at right end), appendleft (insert element at right end)
         pop (delete element from right end), popleft (delete element from left end)

preorder (node-left-right) 
inorder (left-node-right) 
postorder (left-right-node)
