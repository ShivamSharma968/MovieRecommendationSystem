import streamlit as st
import pickle
import pandas as pd

# Load data
movies = pd.read_csv('movies.csv')
cosine_sim = pickle.load(open('cosine_sim.pkl', 'rb'))
svd_model = pickle.load(open('svd_model.pkl', 'rb'))

# Hybrid recommendation function
def recommend(movie, user_id=1):
    idx = movies[movies['title'] == movie].index[0]

    # Content-based scores
    sim_scores = list(enumerate(cosine_sim[idx]))

    scores = []
    for i, content_score in sim_scores:
        movie_Id = movies.iloc[i]['movie_id']

        # SVD predicted rating
        svd_score = svd_model.predict(user_id, movie_Id).est / 5

        # Hybrid score
        final_score = 0.6 * content_score + 0.4 * svd_score

        scores.append((i, final_score))

    # Sort by hybrid score
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Top 5 (skip itself)
    movie_indices = [i[0] for i in scores[1:6]]

    return movies['title'].iloc[movie_indices]


# UI
st.title("🎬 Movie Recommender System (Hybrid)")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)