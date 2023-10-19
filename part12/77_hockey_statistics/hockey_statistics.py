import json


class Player:
    def __init__(
        self,
        name: str,
        nationality: str,
        assists: int,
        goals: int,
        penalties: int,
        team: str,
        games: int,
    ):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def __str__(self):
        return (
            f"{self.name:<20} {self.team} "
            f"{self.goals:>3} + {self.assists:>2} = "
            f"{self.goals + self.assists:>3}"
        )


class Players:
    def __init__(self):
        self.players = []

    def add_player(self, player: Player):
        self.players.append(player)

    def load_players(self, path: str):
        with open(path) as data:
            players = json.loads(data.read())

        for player in players:
            self.add_player(
                Player(
                    player["name"],
                    player["nationality"],
                    player["assists"],
                    player["goals"],
                    player["penalties"],
                    player["team"],
                    player["games"],
                )
            )

    def number_of_players(self):
        return len(self.players)


class AppInterface:
    def __init__(self):
        self.all = Players()

    def print_commands(self):
        print(
            f"commands:\n"
            f"0 quit\n"
            f"1 search for player\n"
            f"2 teams\n"
            f"3 countries\n"
            f"4 players in team\n"
            f"5 players from country\n"
            f"6 most points\n"
            f"7 most goals"
        )

    def load_data(self, path: str):
        self.all.load_players(path)
        print(f"read the data of {self.all.number_of_players()} players\n")


if __name__ == "__main__":
    app = AppInterface()
    app.load_data("partial.json")
    for player in app.all.players:
        print(player)
    app.print_commands()
