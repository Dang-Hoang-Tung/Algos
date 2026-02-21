import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def findK(min_speed: int, max_speed: int) -> int | None:
            if min_speed > max_speed:
                return None

            avg = min_speed + (max_speed - min_speed) // 2
            eating_time = sum([math.ceil(pile / avg) for pile in piles])
            
            if eating_time > h:
                # Too slow, try to find a faster speed
                better_speed = findK(avg + 1, max_speed)
                avg = None
            elif eating_time <= h:
                # Try to find a slower speed
                better_speed = findK(min_speed, avg - 1)

            return better_speed if better_speed else avg
        
        max_speed = max(piles)
        k = findK(1, max_speed)
        return k if k else max_speed
