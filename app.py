import streamlit as st
import pandas as pd
import numpy as np
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=&language=en-US"
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

similarity = np.load('similarity.npy')
def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        recommended_movies.append(df.iloc[i[0]]['title'])
        recommended_movies_posters.append(fetch_poster(df.iloc[i[0]]['movie_id']))
    return recommended_movies,recommended_movies_posters

# Load DataFrame from pickle file
df = pd.read_pickle('movies.pkl')
movies_list = df['title'].values

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'Select a movie from the list',
    movies_list)

if st.button('Recommend me a movie'):
    st.subheader('Recommended movies for you are:')
    names,posters = recommend(selected_movie_name)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.markdown(names[0])
        st.image(posters[0])

    with col2:  
        st.markdown(names[1])
        st.image(posters[1])

    with col3:
        st.markdown(names[2])
        st.image(posters[2])

    with col4:
        st.markdown(names[3])
        st.image(posters[3])

    with col5:
        st.markdown(names[4])
        st.image(posters[4])



