class WaterBottles():
    def num_water_bottles(self, num_bottles: int, num_exchange: int) -> int:
        bottles, remaining = num_bottles, num_bottles
        
        while remaining // num_exchange != 0:
            bottles += remaining // num_exchange
            remaining = remaining % num_exchange + remaining // num_exchange
        return bottles