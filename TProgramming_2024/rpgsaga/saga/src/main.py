from game import Game

if __name__ == "__main__":
    num_players: int = int(input("Введите количество игроков (четное число): "))
    if num_players % 2 != 0:
        print("Количество игроков должно быть четным!")
    else:
        game: Game = Game(num_players)
        game.start()