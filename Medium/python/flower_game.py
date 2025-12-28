class FlowerGame():
    
    def flower_game(self, n: int, m: int):
        return ((n + 1) // 2) * (m // 2) + ((m + 1) // 2) * (n // 2)

if __name__ == "__main__":
    game = FlowerGame()
    
    print(game.flower_game(3,2))
    print(game.flower_game(1,1))