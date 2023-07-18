class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rating = []

    def rate(self, rating: int):
        self.rating.append(rating) if rating >= 0 and rating <= 5 else None

    def __str__(self):
        text = f"{self.title} ({self.seasons} seasons)\n"
        text += f"genres: {', '.join(self.genres)}\n"
        if self.rating:
            text += f"{len(self.rating)} ratings, "
            text += f"average {sum(self.rating) / len(self.rating):.1f} points"
        else:
            text += "no ratings"
        return text


def minimum_grade(rating: float, series_list: list):
    return [s for s in series_list if rating <= sum(s.rating) / len(s.rating)]


def includes_genre(genre: str, series_list: list):
    return [s for s in series_list if genre in s.genres]


if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
