from typing import List

class LatestTime():
    def latest_time_catch_the_bus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        passengers.sort()
        buses.sort()
        top = passengers[len(passengers) - 1]
        bottom = 0
        result = -1

        while top >= bottom:
            mid_time = (top + bottom) // 2
            on_time = self.on_time(buses, passengers, capacity, mid_time)
            print("{} is {}".format(mid_time, on_time))
            if on_time == False:
                top = mid_time - 1
            else:
                if mid_time not in passengers:
                    result = mid_time
                bottom = mid_time + 1
        return result

    
    def on_time(self, buses: List[int], passengers: List[int], capacity: int, time: int) -> bool:
        passenger_list = passengers
        passenger_list.append(time)
        passenger_list.sort()
        bus = 0
        cap = 0
        for passenger in range(len(passenger_list)):
            if bus >= len(buses):
                return False
            if passenger_list[passenger] > buses[bus] or cap == capacity:
                bus += 1
                cap = 0
                passenger += 1
            else:
                if passenger_list[passenger] == time:
                    return True
                cap += 1

if __name__ == "__main__":
     latest_time = LatestTime()

     buses = [10,20]
     passengers = [2,17,18,19]
     capacity = 2

     print(latest_time.latest_time_catch_the_bus(buses, passengers, capacity))
     
     print(latest_time.on_time(buses, passengers, capacity, 14))