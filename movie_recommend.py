import streamlit as st
import pickle
import pandas as pd
import difflib
import requests

movie_data = pickle.load(open("./movierecommendation_trainedmodel.sav", "rb"))
similarity = pickle.load(open("./similarity.sav", "rb"))
movies = pd.DataFrame(movie_data)


def fetch_image(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=02858678f45b0078c4c607453bc55898".format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/original"+data["poster_path"]


def recommend(movie):
    find_close_match = difflib.get_close_matches(
        movie, movies["title"])

    close_match = find_close_match[0]

    index_of_the_movie = movies[movies["title"] ==
                                close_match]['index'].values[0]

    similarity_score = list(enumerate(similarity[index_of_the_movie]))

    sorted_similar_movies = sorted(
        similarity_score, key=lambda x: x[1], reverse=True)[0:5]

    recommended_movies = []
    recommended_movies_images = []
    for i in sorted_similar_movies:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_images.append(fetch_image(movie_id))
    return recommended_movies, recommended_movies_images


def main():
    st.title("Movie Recommendation System")

    selected_movie = st.selectbox("Select your movie", movies["title"].values)

    if st.button("Recommend"):
        recommended_movie_names, recommended_movie_posters = recommend(
            selected_movie)
        num_columns = len(recommended_movie_names)
        columns = st.columns(num_columns)
        # col1, col2, col3, col4, col5, col6 = st.columns(6)
        # columns = [col1, col2, col3, col4, col5, col6]
        for i, col in enumerate(columns):
            with col:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])


if __name__ == '__main__':
    main()
