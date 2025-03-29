class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        count = 1
        #find slope of each point
        for i in range(len(points)):
            standard = points[i]
            c = 0
            slope = {}
            for j in range(len(points)):
                if i == j :
                    continue
                dx = points[j][0] - standard[0] 
                dy = points[j][1] - standard[1]                 
                g = gcd(dx, dy)
                dx //= g
                dy //= g

                if (dx, dy) not in slope:
                    slope[(dx, dy)] = 0

                slope[(dx, dy)]+= 1
                c = max(c , slope[(dx, dy)])

            count = max(count, c + 1)
        return count


                