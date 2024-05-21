import pandas as pd
import joblib

# Adatok betöltése
user_movie_matrix = pd.read_csv('user_movie_matrix.csv', index_col=0)
movies = pd.read_csv('movies.csv')

# Konvertáljuk a movieId oszlopot int típusra
movies['movieId'] = movies['movieId'].astype(int)

# Ellenőrzés
print(user_movie_matrix.head())
print(movies.head())

# Ellenőrizzük, hogy a user_id szerepel-e az adatokban
user_id = 1
if user_id in user_movie_matrix.index:
    print(f"User ID {user_id} found in the user_movie_matrix.")
else:
    print(f"User ID {user_id} not found in the user_movie_matrix.")

# Modell betöltése
model_knn = joblib.load('knn_model.pkl')

# Ajánlások lekérése
distances, indices = model_knn.kneighbors(user_movie_matrix.loc[user_id].values.reshape(1, -1), n_neighbors=6)
print(f"Distances: {distances}")
print(f"Indices: {indices}")

# Ajánlott filmek azonosítói
recommended_movie_ids = user_movie_matrix.columns[indices.flatten()].tolist()
print(f"Recommended Movie IDs: {recommended_movie_ids}")

# Ellenőrizzük, hogy ezek az azonosítók léteznek a movies.csv fájlban
recommended_movies = [movies.loc[movies['movieId'] == int(mid), 'title'].values[0] for mid in recommended_movie_ids if int(mid) in movies['movieId'].values]
print(f"Recommended Movies: {recommended_movies}")
