class SegmentTree(object):  # SegmentTreeNode
    def __init__(self, start, end, value=0):
        self.start = start    # index
        self.end = end        # index
        self.val = value      # val = sum/max/count, etc..
        self.left, self.right = None, None

    @classmethod
    def build(self, start, end, array):
        if start > end:
            return None
    	
        if start == end: # a leaf node
            return SegmentTree(start, end, array[start])

        node = SegmentTree(start, end, array[start])

        mid = (start + end) // 2
        node.left = self.build(start, mid, array)
        node.right = self.build(mid + 1, end, array)
        # lsum, rsum = 0, 0
        # if node.left:
        #     lsum += node.left.val
        # if node.right:
        #     rsum += node.right.val
        # node.sum = lsum + rsum
        node.val = node.left.val + node.right.val
        
        return node # the root

    @classmethod
    def modify(cls, root, index, value):
        if root is None:
            return

        if root.start == root.end:
            root.val = value
            return
    
        if root.left.end >= index:
            cls.modify(root.left, index, value)
        else:
            cls.modify(root.right, index, value)
        
        root.val = root.left.val + root.right.val

    @classmethod
    def query(cls, root, start, end):
        if root.start > end or root.end < start:
            return 0
    
        if start <= root.start and root.end <= end:   # why <= not ==?
            return root.val
        
        return cls.query(root.left, start, end) + cls.query(root.right, start, end)