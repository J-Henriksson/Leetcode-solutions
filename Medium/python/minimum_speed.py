from typing import List
import math

class MinimumSpeed():
    def min_Speed_on_time(self, dist: List[int], hour: float) -> int:
        top = int(1e7) #This seems like such an arbitrary and inefficient way to set the top, but doesn't seem like there's another way to go about it.
        bottom = 1
        result = -1

        while top >= bottom:
            mid_speed = (top + bottom) // 2
            time_for_speed = self.time_to_travel(dist, mid_speed)
            #print("speed = {} time = {}".format(mid_speed, time_for_speed))
            #If time is too small speed must decrease
            #If time is too big speed must increase
            if time_for_speed > hour:
                bottom = mid_speed + 1
            else:
                result = mid_speed
                top = mid_speed - 1
        return result


    def time_to_travel(self, dist: List[int], speed: int) -> int:
        time = 0
        for ride in range(len(dist)):
            if ride == len(dist) - 1:
                time += float(dist[ride]) / speed
            else:
                time += math.ceil(float(dist[ride]) / speed)
        return time

if __name__ == "__main__":
    min_speed = MinimumSpeed()
    dist_1 = [1,3,2]
    dist_2 = [1,1,100000]

    print(min_speed.min_Speed_on_time(dist_1, 6))
    print(min_speed.min_Speed_on_time(dist_1, 2.7))
    print(min_speed.min_Speed_on_time(dist_1, 1.9))
    print(min_speed.min_Speed_on_time(dist_2, 2.01))