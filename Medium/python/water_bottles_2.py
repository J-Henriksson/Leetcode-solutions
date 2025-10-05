class WaterBottles2():
    def num_water_bottles(self, num_bottles: int, num_exchange: int) -> int:
        bottles, remaining, exchange = num_bottles, num_bottles, num_exchange
        
        while remaining // exchange != 0:
            bottles += 1
            remaining -= (exchange - 1)
            exchange += 1
        return bottles