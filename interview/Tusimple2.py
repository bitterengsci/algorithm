#coding=utf-8
import sys 

'''
给一个整数n，只能对这个数进行+1会或-1操作，问最少多少次操作后能将这个数的每一位都变成偶数，例如

42 => 0

11 => 3

1 => 1

1356 -> 468
9
2000
0888
2356 -> 44


'''

# 111 -> 88 111-88 = 23
# 777 -> 800 
# abcd
# a -> even, bcd -> odd type
# a -> odd, bcd, b > 44  +, < 44 -
#        b = 44, 

# 100 ~ 199  -> 200, 88 - > 144

# N 
# N // 10 -> 0 --> 1 time or 0 time
# N > 0, highest = N // 10, highest -> odd (need change),
#                            highest -> even, N % 10
# 1356 // 10 -> 135 > 0 
# highest = 1 (odd)
# 356 < 444 (minus)
# 888
# 1356 - 888  = 468

def times_of_change(num):
    if num // 10 == 0:   
        if num % 2: # odd
            return 1
        else: # even
            return 0
        
    magnitude = len(str(num)) - 1
    highest = int(str(num)[0])
    reminder = num - highest * 10 ** magnitude
    
    if highest == 9:
        return num - int(str('8') * (magnitude + 1))
    
    if highest % 2: # odd, 1, 3, 5, 7
        if reminder >= int(str('4') * magnitude): # add
           return (highest + 1) * 10 ** magnitude - num
        else: # subtract
           return num - int(str('8') * magnitude) - (highest - 1) * 10 ** magnitude
    else:   # even
        return times_of_change(reminder)
    
print(times_of_change(1356))
print(times_of_change(2356))
print(times_of_change(8))
print(times_of_change(9))
print(times_of_change(99)) # -> 88
print(times_of_change(999)) # -> 888
print(times_of_change(799)) # -> 800
print(times_of_change(521)) # -> 488
print(times_of_change(544)) # -> 488, 600
print(times_of_change(543)) # -> 488
print(times_of_change(545)) # -> 600



'''
给定搜索二叉树，构造出一棵平衡搜索二叉树
[1,2,3,4,5,7,8]
'''

class Tree():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right
        
    # def is_leaf(self):
        # return True if self.left is None and self.right is None else False

def balance_binary_tree(root):
    # 1. traverse the tree and fetch all the node values
    nodes = []
    traverse(root, nodes)
    
    # 2. reconstruct a balanced binary tree
    return reconstruct(nodes)
    
def traverse(root, nodes):
    if root is None:
        return 
    traverse(root.left, nodes)
    nodes.append(root.val)
    traverse(root.right, nodes)
    
def reconstruct(nodes):
    if not nodes: # list is empty
        return  # return None
    median_idx = len(nodes) // 2
    root = Tree(nodes[median_idx], reconstruct(nodes[:median_idx]), reconstruct(nodes[median_idx+1:]))

    return root


def test(nodes):
    root = reconstruct(nodes)
    
    new_nodes = []
    traverse(root, new_nodes)
    print(nodes)
    print(new_nodes)
    
test([1, 1, 2])



'''

[[0,1],

 [1,0]] => 2

[[0,1,0],

 [0,0,0],

 [0,0,1]] => 3

[[1,1,1,1,1],

 [1,0,0,0,1],

 [1,0,1,0,1],

 [1,0,0,0,1],

 [1,1,1,1,1]] => 2


0,0,0,0
0,1,0,0
0,0,0,0
0,0,0,1

[[0,0,0,0,1],
 [0,0,1,0,1],
 [0,1,1,0,1],
 [1,0,0,0,1],
 [1,1,1,1,1]] => 2

'''

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def min_distance(mat):
    R, C = len(mat), len(mat[0])
    # first block = 1
    # second block = 2
    # block1, block2   # list of node
    queue = block1
    distance = 0
    
    visited = [[False for _ in range(C)] for _ in range(R)]
    
    while not any([pos if pos in block2 for pos in queue]):
        next_queue = []
        for pos in queue:
            for d in delta:
                x, y = pos[0] + d[0], pos[1] + d[1]
                if R > x >= 0 and C > y >= 0 and mat[x][y] != 1 and not visited[x][y]: # valid step
                    next_queue.append([x, y])
                    visited[x][y] = True

        distance += 1
        queue = next_queue

    return distance