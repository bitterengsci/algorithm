# 单调递减栈
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree1(self, A):
        if not A:
            return None
            
        nodes = [TreeNode(num) for num in A + [sys.maxsize]]
        stack = []
        for index, num in enumerate(A + [sys.maxsize]):
            while stack and A[stack[-1]] < num:
                top = stack.pop()
                left = A[stack[-1]] if stack else sys.maxsize
                if left < num:
                    nodes[stack[-1]].right = nodes[top]
                else:
                    nodes[index].left = nodes[top]
            
            stack.append(index)

        # sys.maxsize 's left child is the maximum number
        return nodes[-1].left
        
    def maxTree2(self, A):
        stack = []
        for num in A:
            node = TreeNode(num)		#新建节点
            while stack and num > stack[-1].val:		#如果stk中的最后一个节点比新节点小
                node.left = stack.pop()					#当前新节点的左子树为stk的最后一个节点
                
            if stack:									#如果stk不为空
                stack[-1].right = node					#将新节点设为stk最后一个节点的右子树
                
            stack.append(node)

        return stack[0]

    """
    单调栈可以在O(n)的时间里跑出以每个元素作为最大/小值的最左/右端点下标。
    单调栈的操作：
        以一个递减的单调栈为例，若栈为空或者栈顶元素大于当前元素则压入，
        否则弹出栈内比当前元素小的所有元素。
    
    {7， 2， 5， 3， 11， 9}
    第一步：栈为空，压入7          此时栈内：[7]
    第二步：7比2大，压入2          此时栈内：[7, 2]
    第三步：2比5小，弹出2，压入5   此时栈内：[7, 5]
    第四步：5比3大，压入3          此时栈内：[7, 5, 3]
    第五步：3、5、7 比11小，弹出3、弹出5、弹出7，压入11    此时栈内：[11]
    第六步：11比9大，压入9         此时栈内：[11, 9]
    在这个过程中可以发现，栈底元素是栈内元素中的最大值，而最后留在栈内的最底部的元素就是整个数组中的最大元素root。一个元素作为节点时的左儿子也就是左半边最大的值，是这个元素被压入栈时，栈弹出的最后一个元素；而右儿子也就是右半边最大的值，是这个元素的上面一个元素，因为递减的单调栈是从底部往顶部依次减小的。
    
    具体实现：
        - 从前往后依次遍历数组元素，对每个元素：
        - 如果栈内有元素且小于当前元素，那么依次弹出栈内比当前元素小的元素。
            在这个过程中记录最后一个被弹出的元素，这个元素就是当前元素的左儿子
        - 如果栈内有元素且栈顶元素大于当前元素，那么当前元素就是栈顶元素的右儿子
        - 最后压入当前元素
    所以我们很容易在这个过程中得到答案，也就是{11,7,9,#,5,#,#,2,3}
    """
    def maxTree3(self, A):
        n = len(A)
        stack = [0] * n
        cnt = -1
        pNodes = []
        for i in range(0, n):
            node = TreeNode(A[i])
            pNodes.append(node)
            if cnt > -1 and A[stack[cnt]] < A[i]:
                # 如果栈中有元素且元素小于当前元素，则弹出栈内元素
                while cnt > -1 and A[stack[cnt]] < A[i]:
                    cnt -= 1
                # 弹出的最后一个元素就是当前元素的左儿子
                pNodes[i].left = pNodes[stack[cnt + 1]]
            if cnt > -1 and A[stack[cnt]] > A[i]:
                # 如果栈内有元素且栈顶元素大于当前元素
                # 那么当前元素是栈顶元素的右儿子
                pNodes[stack[cnt]].right = pNodes[i]
            # 压入当前元素
            cnt += 1
            stack[cnt] = i
        return pNodes[stack[0]]


    # 分治(TLE)
    """
    根结点是整个数组中最大的值。根结点把整个区间分成两个部分，
    左边是左子树，右边是右子树，因此我们很容易想到分治。
    找到根结点，然后我们再分别往下递归寻找到左子树的根结点，右子树的根结点即可
    
    复杂度
    空间复杂度为O(n);
    最坏的情况每次寻找最小值时需要O(n+n-1+n-2+...+1)，时间复杂度为O(n^2)。
    因此数据比较小时可以，数据大了要换时间复杂度小的算法，比如O(n)的单调栈
    """
    # 寻找左/右儿子
    def dfs(self, left, right, A):
        pos = left
        for i in range(left, right + 1):
            if A[i] > A[pos]:
                pos = i
        son = TreeNode(A[pos])
        # 如果有的话，寻找son的左/右儿子
        if left < pos:
            son.left = self.dfs(left, pos - 1, A)
        if right > pos:
            son.right = self.dfs(pos + 1, right, A)
        return son
    
    def maxTree(self, A):
        n = len(A)
        # pos表示当前区间最大值的下标
        pos = 0
        for i in range(n):
            if A[i] > A[pos]:
                pos = i
        # 根结点
        root = TreeNode(A[pos])
        if pos > 0:
            # 左儿子
            root.left = self.dfs(0, pos - 1, A)
        if pos < n - 1:
            # 右儿子
            root.right = self.dfs(pos + 1, n - 1, A)
        return root