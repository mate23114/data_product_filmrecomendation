from flask import Flask, request, jsonify
import pandas as pd
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Engedélyezi a CORS-t az összes útvonalhoz

# Modell és adatok betöltése a 'data' mappából
model_knn = joblib.load('data/knn_model.pkl')
user_movie_matrix = pd.read_csv('data/user_movie_matrix.csv', index_col=0)
movies = pd.read_csv('data/movies.csv')

# Konvertáljuk a movieId oszlopot int típusra
movies['movieId'] = movies['movieId'].astype(int)

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        user_id = int(request.json['user_id'])
        if user_id not in user_movie_matrix.index:
            return jsonify({"error": "User ID not found"}), 400

        distances, indices = model_knn.kneighbors(user_movie_matrix.loc[user_id].values.reshape(1, -1), n_neighbors=6)
        recommended_movie_ids = user_movie_matrix.columns[indices.flatten()].tolist()
        recommended_movies = [movies.loc[movies['movieId'] == int(mid), 'title'].values[0] for mid in recommended_movie_ids if int(mid) in movies['movieId'].values]

        return jsonify(recommended_movies)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
