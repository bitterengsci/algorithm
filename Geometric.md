

# Geometric Algorithm

Closest Pair of Points
- divide and conquer TC=O(n(logn)^2)
- TC=O(nlogn)


Two line segments intersect



Points inside/outside a polygon (convex/non-convex)
- Draw a horizontal line to the right of each point and extend it to infinity.
- Count the number of times the line intersects with polygon edges.
- A point is inside the polygon if either count of intersections is odd or point lies on an edge of polygon.


Convex Hull
- Given a set of points, the convex hull of the set is the smallest convex polygon that contains all the points of it.


Given n line segments, find if any two segments intersect
- Sweep Line TC=O(nlogn)


A given point lies inside a triangle or not
- coordinates of the corners of triangle: (x1, y1), (x2, y2), (x3, y3)
- area of triangle: A = abs( x1 * (y2 – y3) + x2 * (y3 – y1) + x3 * (y1 - y2) ) / 2
- if area of the triangle = PAB + PAC + PBC, then 


if given four points form a square
- a) All fours sides formed by points are the same. 
- b) The angle between any two sides is 90 degree. (This condition is required as Quadrilateral also has same sides. 
- c) Check both the diagonals have the same distance



# Mathematical Algorithm

if a number is multiple of 11
- If difference between sum of odd digits and even digits is multiple of 11 then decimal number is multiple of 11
- AB = 11A - A + B = 11A + (B – A), if (B – A) is a multiple of 11 then is AB
- ABC = 99A + A + 11B – B + C = (99A + 11B) + (A + C – B), if (A + C – B) is a multiple of 11 then is ABC
- Analogously can be applied to multiple of 3 in binary format

Multiply with 7 (for positive numbers)
- using bitwise operator: left shift (<<) the number by 3 bits (=8n) then subtract the original number from the shifted number and return the difference (8n – n)

Lucky Numbers
- Take the set of integers 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,...
- First, delete every second number, we get following reduced set: 1,3,5,7,9,11,13,15,17,19,...
- Now, delete every third number, we get 1, 3, 7, 9, 13, 15, 19,...
- Continue this process indefinitely. Any number that does NOT get deleted due to above process is called "lucky".
```python
def isLucky(n, counter):    # counter = 2 initially
    if counter > n:
        return True
    if n % counter == 0:
        return False
     
    return isLucky(n - (n // counter), counter + 1)

isLucky(5, 2)  # False
isLucky(19, 2) # True
```

