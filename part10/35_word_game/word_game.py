import random


class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        if len(player2_word) > len(player1_word):
            return 2
        return None


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        p1 = sum(player1_word.count(vowel) for vowel in "aeiou")
        p2 = sum(player2_word.count(vowel) for vowel in "aeiou")
        if p1 > p2:
            return 1
        if p2 > p1:
            return 2
        return None


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        rps = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
        if player1_word not in rps:
            return 2 if player2_word in rps else None
        if player2_word not in rps:
            return 1
        if rps[player1_word] == player2_word:
            return 1
        if rps[player2_word] == player1_word:
            return 2
        return None


if __name__ == "__main__":
    p = RockPaperScissors(4)
    p.play()
