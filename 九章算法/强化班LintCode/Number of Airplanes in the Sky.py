"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        points = []
        for airplane in airplanes:
            points.append([airplane.start, 1])  # takeoff
            points.append([airplane.end, -1])   # land
        
        
        # sweep line
        number_of_airplane, max_number_of_airplane = 0, 0
        for _, count_delta in sorted(points):
            number_of_airplane += count_delta
            max_number_of_airplane = max(max_number_of_airplane, number_of_airplane)
            
        return max_number_of_airplane