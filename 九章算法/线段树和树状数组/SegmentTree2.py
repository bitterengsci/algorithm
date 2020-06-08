class SegmentTree(object):  # SegmentTreeNode
    def __init__(self, start, end, value=0):
        self.start, self.end = start, end   # index
        self.val = value      # val = sum/max/count, etc..
        self.left, self.right = None, None

    def build(self, start, end, array):
        if start > end:
            return None
    	
        if start == end: # a leaf node
            return SegmentTree(start, end, array[start])

        node = SegmentTree(start, end, array[start])

        mid = (start + end) // 2
        node.left = self.build(start, mid, array)
        node.right = self.build(mid + 1, end, array)

        node.val = node.left.val + node.right.val
        
        return node # the root

    def modify(self, root, index, value):
        if root is None:
            return

        if root.start == root.end:
            root.val = value
            return
    
        if root.left.end >= index:
            self.modify(root.left, index, value)
        else:
            self.modify(root.right, index, value)
        
        root.val = root.left.val + root.right.val

    def query(self, root, start, end):
        if root.start > end or root.end < start:
            return 0
    
        if start <= root.start and root.end <= end:
            return root.val
        
        return self.query(root.left, start, end) + self.query(root.right, start, end)