class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        m = len(image)
        if m == 0:
            return 0
        n = len(image[0])
        if n == 0:
            return 0

        start, end = y, n - 1
        while start < end:
            mid = start + (end - start) // 2 + 1
            if self.checkColumn(image, mid):
                start = mid
            else:
                end = mid - 1
        right = start

        start, end = 0, y
        while start < end:
            mid = start + (end - start) // 2
            if self.checkColumn(image, mid):
                end = mid
            else:
                start = mid + 1
        left = start

        start, end = x, m - 1
        while start < end:
            mid = start + (end - start) // 2 + 1
            if self.checkRow(image, mid):
                start = mid
            else:
                end = mid - 1
        down = start

        start, end = 0, x
        while start < end:
            mid = start + (end - start) // 2
            if self.checkRow(image, mid):
                end = mid
            else:
                start = mid + 1
        up = start

        return (right - left + 1) * (down - up + 1)

    def checkColumn(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return True
        return False
        # return any(image[i][col] == '1' for i in range(len(image)))   # works poorly than the uncommented one

    def checkRow(self, image, row):
        for j in range(len(image[0])):
            if image[row][j] == '1':
                return True
        return False
        # return any(image[row][j]=='1' for j in range(len(image[0])))