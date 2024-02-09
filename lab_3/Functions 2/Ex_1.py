def is_movie_imdb_above(movie : str) -> bool:
    from Ex2 import movies

    for m in movies:
        if m["name"] == movie:
            return m["imdb"] > 5.5
    
    return False
print(is_movie_imdb_above("AlphaJet"))


def is_movie_imdb_above() -> list:
    from Ex2 import movies
    above_5_5 = []

    for m in movies:
        if m["imdb"] > 5.5:
            above_5_5.append(m["name"])
    
    return above_5_5
print(is_movie_imdb_above())


def is_movie_imdb_above(category : str) -> list:
    from Ex2 import movies
    same_categories = []

    for m in movies:
        if m["category"] == category:
            same_categories.append(m["name"])
    
    return same_categories
print(is_movie_imdb_above("War"))


def average_imdb_score(movies : list) -> float:
    score_overall = 0
    for movie in movies:
        score_overall += movie["imdb"]

    return score_overall / len(movies)

from Ex2 import movies
print(average_imdb_score(movies))


def average_imdb_score(category : str) -> float:
    score_overall, count = 0, 0
    for movie in movies:
        if movie["category"] == category:
            score_overall += movie["imdb"]
            count += 1

    return score_overall / count
from Ex2 import movies
print(average_imdb_score("Romance"))