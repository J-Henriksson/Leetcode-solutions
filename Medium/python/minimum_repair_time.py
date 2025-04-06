class MinimumRepairTime():

    def repair_cars(self, ranks, cars):
        ranks.sort()
        top = ranks[0] * (cars**2)
        bottom = 1
        result = 0
        while top >= bottom:
            mid = (top + bottom) // 2
            mid_cars = self.cars_for_time(ranks, mid)

            if mid_cars < cars:
                bottom = mid + 1
            else:
                result = mid
                top = mid - 1
        return result
    
    def cars_for_time(self, ranks, time):
        car_sum = 0
        for rank in ranks:
            car_sum += int((time / rank)**0.5)
        return car_sum
    

if __name__ == "__main__":
    repair_calc = MinimumRepairTime()
    ranks = [4,2,3,1]
    cars = 10

    print(repair_calc.repair_cars(ranks, cars))