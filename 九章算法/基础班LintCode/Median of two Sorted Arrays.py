class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    # Approach: 归并排序
    '''
    将两个数组合并, 然后返回新数组的中位数。两个有序数组的合并也是经典归并排序算法的一步, 我们可以新开一个数组, 保存合并后的结果。但是我们这样会做额外的工作, 因为我们不必保存整个新数组, 只需要知道新数组的中位数即可
    双指针分别对两个数组遍历, 比较两个指针下的元素大小, 每次移动更小的指针, 通过移动次数确定中位数的位置
    算法流程:
     * 令指针p1和p2分别指向两个数组, 初始指向位置0。需遍历(m + n)/2 + 1次, 每次比较两个位置的元素, 在第k次比较时, 较小的那个值就是两个数组中第k + 1小的数。如果一个指针已经走到了数组末尾, 那么移动另一个指针, 否则每次将指向较小数的指针后移, 直到遍历到中位数。
     * 为了将奇偶情况合并, 在代码中用了left和right保存中间值, 如果是奇数直接返回right, 如果是偶数就返回(left + right) / 2。
    
    时间复杂度：O(m+n) 双指针遍历两个数组, 指针移动次数是0(m+n)级   空间复杂度：O(1)
    '''
    def findMedianSortedArrays1(self, A, B):
        p1, p2 = 0, 0
        left, right = -1, -1 
        for _ in range((len(A) + len(B)) // 2 + 1):
            left = right   # left是前一个值
            if p1 >= len(A) or p2 < len(B) and A[p1] > B[p2]: # p2 右移
                right = B[p2]
                p2 += 1
            else: # p1 右移
                right = A[p1]
                p1 += 1
        
        if (len(A) + len(B)) % 2 == 1:   # 长度和是奇数
            return right
        return (left + right) / 2        # 长度和是偶数
    
    
    # Approach: 二分 binary search
    # overall run time complexity should be O(log (m+n))
    '''
    利用数组的有序性, 就能一半一半的排除; 假设我们要找第k小数, 通过二分, 可以每次循环排除掉k/2个数
    
    算法流程:
    * 建立辅助函数getKth, 目标是找到A[start1:end1]和B[start2:end2]中第k小的元素
    * 主程序中, 看m + n的奇偶性, 并调用getKth函数
        - 如果是奇数, 返回数组A和B的第(m + n) // 2 + 1小元素
        - 如果是偶数, 返回数组A和B的第(m + n) // 2小和第(m + n) // 2 + 1小元素的均值
    * getKth(nums1, start1, end1, nums2, start2, end2, k)函数的实现方法:
        - 如果有数组在[start:end]范围内为空, 说明该数组已经排除完毕, 第k小的元素一定存在于另一数组中, 计算好索引位置返回即可 
        - 如果k为1, 说明已经找到第k小的数, 那就是A[start1]和B[start2]中的较小值, 直接返回即可
        - 定义指针i和j, 分别指向A和B, 使得A[start1:i]和B[start2:j]的长度分别为k // 2, 通过比较A[i]和B[j]的大小, 我们就可以确定排除哪段元素
        - 如果A[i] > B[j], 说明B[start2:j]不可能为第k小元素。我们对A[start1:end1]和B[j + 1:end2]继续送入getKth进行递归, k应该更新为k - (j - start2 + 1)
        - 反之, 说明A[start1:i]不可能为第k小元素。我们对A[i + 1:end1]和B[start2:end2]继续送入getKth进行递归, k应该更新为k - (i - start1 + 1)
    
    时间复杂度：O(log(m+n)), m和n分别是两个数组的长度。二分法的复杂度为 O(log(m+n))   空间复杂度：O(1)
    '''
    def findMedianSortedArrays2(self, A, B):
        # 如果是奇数
        if (len(A) + len(B)) % 2 == 1:
            return self.getKth(A, 0, len(A) - 1, B, 0, len(B) - 1, (len(A) + len(B)) // 2  + 1)
        # 如果是偶数
        return (self.getKth(A, 0, len(A) - 1, B, 0, len(B) - 1, (len(A) + len(B)) // 2) + self.getKth(A, 0, len(A) - 1, B, 0, len(B) - 1, (len(A) + len(B)) // 2 + 1)) / 2

    def getKth(self, A, start1, end1, B, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        # 让 len1 的长度小于 len2, 这样就能保证如果有数组空了, 一定是 len1 
        if len1 > len2: 
            return self.getKth(B, start2, end2, A, start1, end1, k)
        # A数组排除完毕
        if len1 == 0:
            return B[start2 + k - 1]
        # 已经找到第k小的数
        if k == 1:
            return min(A[start1], B[start2])
            
        # 开始二分
        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1
        if (A[i] > B[j]):
            return self.getKth(A, start1, end1, B, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.getKth(A, i + 1, end1, B, start2, end2, k - (i - start1 + 1))
            
    # Approach: 快速选择
    '''
    对于长度为m的数组A, 我们把A划分成两个部分A1 = A[0, i-1]和A2 = A[i, m-1]; 对于长度为n的数组B, 将B划分成B1 = B[0, j-1]和B2 = B[j, n-1], 使得len(A1) + len(B1) == len(A2) + len(B2)（条件1） (当A划分后, B的划分位置就是确定的)
    如果能够确定max(A1[:], B1[:]) <= min(A2[:], B2[:])（条件2）, 说明已经找到合适的划分, 能够把{A, B}分成长度相等的两份, 且一份中的元素全部大于等于另一份。
    中位数就为(max(A1[:], B1[:]) + min(A2[:], B2[:])) / 2
    怎么找到满足条件2的划分呢？
    选择较短的数组, 假设长度为m, 对它可能的划分位置有m + 1种, 进行二分搜索, 时间复杂度能够进一步优化到 O(log(min(m,n))
    
    算法流程: 
    * 如果A长度大于B, 两者交换一下, 保证A是更短的。
    * 对A进行二分, low和high初始化为0和m, 每次循环不断缩小二分区间 对A的划分位置partition_x为区间中点low + (high - low) // 2, 根据条件1计算出B的划分位置partition_y
        在划分处的两端, 可以得到四个值：A左部分的最大值max_left_x, A右部分的最小值min_right_x, B左部分的最大值max_left_y, B右部分的最小值min_right_y
        如果某个值不存在, 对于这种边界情况, 我们把最大值设为无穷小, 最小值设为无穷大, 保证后一步的比较恒成立 
        - 如果划分满足条件2, 用上述四值来翻译一下就是max_left_x <= min_right_y and max_left_y <= min_right_x:, 那么我们就找到了中位数, 是max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
        - 如果不满足, 如果max_left_x > min_right_y, 说明partition_x位置靠右了, 令high = partition_x - 1；反之, 说明partition_x位置靠左了, 令low = partition_x + 1。继续循环。
    
    时间复杂度：O(log(min(m,n))。m和n分别是两个数组的长度     空间复杂度：O(1)
    '''
    def findMedianSortedArrays(self, A, B):
        # if input1 length is greater than switch them so that input1 is smaller than input2
        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)
        
        m, n = len(A), len(B)
        low, high = 0, m

        while low <= high:
            partition_x = low + (high - low) // 2
            partition_y = (m + n + 1)// 2 - partition_x
            
            # if partition_x is 0 it means nothing is there on left side. Use -INF for max_left_x
            if partition_x == 0:
                max_left_x = float('-inf')
            else:
                max_left_x = A[partition_x - 1]
            
            # if partition_x is length of input then there is nothing on right side. Use +INF for min_right_x
            if partition_x == m:
                min_right_x = float('inf')
            else:
                min_right_x = A[partition_x]
            
            if partition_y == 0:
                max_left_y = float('-inf')
            else:
                max_left_y = B[partition_y - 1]
            
            if partition_y == n:
                min_right_y = float('inf')
            else:
                min_right_y = B[partition_y]
            
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # Now get max of left elements and min of right elements to get the median in case of even length combined array size
                if (m + n) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                # or get max of left for odd length combined array size.
                else:
                    return max(max_left_x, max_left_y)
            # we are too far on right side for partitionX. Go on left side. 
            elif max_left_x > min_right_y:
                high = partition_x - 1
            # we are too far on left side for partitionX. Go on right side.
            else:
                low = partition_x + 1
        return 0
        