import pandas as pd

# Adatok betöltése a 'data' mappából
movies = pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv')
tags = pd.read_csv('data/tags.csv')
links = pd.read_csv('data/links.csv')

# Adatok vizsgálata
print(movies.head())
print(ratings.head())

# Hiányzó értékek kezelése
movies = movies.dropna()
ratings = ratings.dropna()

# Pivot tábla létrehozása a felhasználói értékelések alapján
user_movie_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')

# Hiányzó értékek kitöltése 0-val
user_movie_matrix = user_movie_matrix.fillna(0)

# A pivot tábla mentése a további felhasználáshoz
user_movie_matrix.to_csv('data/user_movie_matrix.csv')
