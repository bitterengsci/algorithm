class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    # Approach: 双指针
    def intersection(self, nums1, nums2):
        intersect = []
        
        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersect.append(nums1[i])
                i += 1
                j += 1            
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
            
        return intersect
        
        
    # list(set(nums1) & set(nums2))
    # [x for x in set(nums1) if x in set(nums2)]
    
    # Approach: 二分查找
    # 首先, 将nums1排序
    # 对于nums2中的每个元素，在有序的nums1中进行二分查找，如果找到，加入intersect集合中
    # 将集合intersect的元素移入res中