from sklearn.neighbors import NearestNeighbors
import pandas as pd
import joblib

# Adatok betöltése
user_movie_matrix = pd.read_csv('data/user_movie_matrix.csv', index_col=0)

# KNN modell építése
model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
model_knn.fit(user_movie_matrix.values)

# Modell mentése
joblib.dump(model_knn, 'data/knn_model.pkl')
