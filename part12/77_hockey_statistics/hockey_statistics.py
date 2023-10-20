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

    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:<20} {self.team} {self.goals:>3} + {self.assists:>2} = {self.points():>3}"


class Players:
    def __init__(self):
        self.players = []

    def load_data(self, path: str):
        with open(path) as data:
            return json.loads(data.read())

    def add_players(self, players_data: list):
        for player in players_data:
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

    def add_player(self, player: Player):
        self.players.append(player)

    def number_of_players(self):
        return len(self.players)

    def search_player(self, name: str):
        player = filter(lambda player: player.name == name, self.players)
        return next(player, "No such a player")

    def teams(self):
        teams = map(lambda player: player.team, self.players)
        return sorted(set(teams))

    def countries(self):
        countries = map(lambda player: player.nationality, self.players)
        return sorted(set(countries))

    def order_by_points(self, player: Player):
        return (player.points(), player.goals)

    def search_team(self, team: str):
        players = list(filter(lambda player: player.team == team, self.players))
        return sorted(players, key=self.order_by_points, reverse=True)

    def search_country(self, country: str):
        players = list(filter(lambda p: p.nationality == country, self.players))
        return sorted(players, key=self.order_by_points, reverse=True)

    def order_by_goals(self, player: Player):
        return (player.goals, -player.games)

    def search_goal_players(self, number: int):
        return sorted(self.players, key=self.order_by_goals, reverse=True)[:number]

    def search_points_players(self, number: int):
        return sorted(self.players, key=self.order_by_points, reverse=True)


class AppInterface:
    def __init__(self):
        self.all = Players()

    def load_data(self, path: str):
        data = self.all.load_data(path)
        self.all.add_players(data)
        print(f"read the data of {len(self.all.players)} players\n")

    def print_player(self, name: str):
        print()
        print(self.all.search_player(name))

    def print_teams(self):
        for team in self.all.teams():
            print(team)

    def print_countries(self):
        for country in self.all.countries():
            print(country)

    def print_team_players(self, name: str):
        print()
        for player in self.all.search_team(name):
            print(player)

    def print_country_players(self, name: str):
        print()
        for player in self.all.search_country(name):
            print(player)

    def print_goal_players(self, number: int):
        print()
        for player in self.all.search_goal_players(number):
            print(player)

    def commands(self):
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

    def run(self):
        get_path = input("file name: ")
        self.load_data(get_path)
        self.commands()
        while True:
            command = input("\ncommand: ")
            if command == "0":
                break
            if command == "1":
                get_name = input("name: ")
                self.print_player(get_name)
            if command == "2":
                self.print_teams()
            if command == "3":
                self.print_countries()
            if command == "4":
                get_name = input("team: ")
                self.print_team_players(get_name)
            if command == "5":
                get_name = input("country: ")
                self.print_country_players(get_name)
            if command == "6":
                break
            if command == "7":
                get_number = int(input("how many: "))
                self.print_goal_players(get_number)


if __name__ == "__main__":
    app = AppInterface()
    app.run()
