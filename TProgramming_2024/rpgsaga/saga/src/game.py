import random
from typing import List
from heroes.hero_factory import HeroFactory
from heroes.hero import Hero

class Game:
    def __init__(self, num_players: int) -> None:
        self.num_players: int = num_players
        self.names: List[str] = ["Артур", "Эльдар", "Геральт", "Пётр", "Лавилас", "Гарри", "Дамблдор", "Аркадий"]
        self.players: List[Hero] = self._create_players()

    def _create_players(self) -> List[Hero]:
        players: List[Hero] = []
        for _ in range(self.num_players):
            name: str = random.choice(self.names)
            self.names.remove(name)  
            health: int = random.randint(50, 100)
            strength: int = random.randint(5, 20)
            hero_type: str = random.choice(["Knight", "Archer", "Mage"])
            players.append(HeroFactory.create_hero(hero_type, name, health, strength))
        return players

    def _fight(self, player1: Hero, player2: Hero) -> Hero:
        while player1.is_alive() and player2.is_alive():
            # Игрок 1 ходит
            if random.choice([True, False]):  # Случ выбор атака или способность
                player1.use_ability(player2)
            else:
                player1.attack(player2)

            if not player2.is_alive():
                break

            # Игрок 2 ходит
            if random.choice([True, False]):  # Случ выбор атака или способность
                player2.use_ability(player1)
            else:
                player2.attack(player1)

        return player1 if player1.is_alive() else player2

    def start(self) -> None:
        round_num: int = 1
        while len(self.players) > 1:
            print(f"\n--- Раунд {round_num} ---")
            winners: List[Hero] = []
            random.shuffle(self.players)  # Ранд перемешивание игроков

            for i in range(0, len(self.players), 2):
                player1: Hero = self.players[i]
                player2: Hero = self.players[i + 1]
                print(f"({player1.__class__.__name__}) {player1.name} vs ({player2.__class__.__name__}) {player2.name}")

                winner: Hero = self._fight(player1, player2)
                winners.append(winner)
                print(f"Победитель: ({winner.__class__.__name__}) {winner.name}")

            self.players = winners
            round_num += 1

        print(f"\n🏆 Победитель турнира: ({self.players[0].__class__.__name__}) {self.players[0].name} 🏆")