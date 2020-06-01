class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        if not k: return []
        
        closest_number = self.closest_number(A, target)
        print("closest_number=", closest_number)
        
        res = [A[closest_number]]
        i, j = closest_number - 1, closest_number + 1

        while len(res) < k:
            if i >= 0 and j < len(A):
                if abs(A[i] - target) <= abs(A[j] - target):
                    res.append(A[i])
                    i -= 1
                else:
                    res.append(A[j])
                    j += 1
            elif i < 0 and j < len(A):
                res.append(A[j])
                j += 1
                
            elif i >= 0 and j >= len(A):
                res.append(A[i])
                i -= 1
        
        return res
    
    def closest_number(self, A, target):
        if not A: return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                return mid
            elif A[mid] > target: # find the one closest to and smaller than target first
                end = mid
            else:
                start = mid

        if abs(A[end] - target) < abs(target - A[start]):
            return end
        else:
            return start
            
        
