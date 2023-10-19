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
        return len(self.players)


class AppInterface:
    def __init__(self):
        self.all = Players()

    def load_data(self, path: str):
        loaded = self.all.add_players(path)
        print(f"read the data of {loaded} players")


if __name__ == "__main__":
    app = AppInterface()
