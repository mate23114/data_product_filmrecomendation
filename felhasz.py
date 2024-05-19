import pandas as pd

# Betöltjük az adatokat
ratings = pd.read_csv('ratings.csv')

# Az első felhasználó értékelései
user_1_ratings = ratings[ratings['userId'] == 1]
print(user_1_ratings)
