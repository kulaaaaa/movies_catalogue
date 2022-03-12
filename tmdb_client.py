from flask import Flask
import requests
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyN2I3Nzk5ZjI3ODVhNDExZWJmZWRjOTkwYTRlYjZkNyIsInN1YiI6IjYyMjhkZThiYzE2MDZhMDA2N2RjYjIyMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TF2CRrS8ldMVwpi8jO-FF0ZDfwggxw6yFHvchSZl7l4"

app = Flask(__name__)

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()

#def get_movies_list(list_type):
#    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
#    headers = {"Authorization": f"Bearer {API_TOKEN}"}
#    response = requests.get(endpoint, headers=headers)
#    response.raise_for_status()
#    return response.json()

def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")

def get_poster_url(poster_api_path, poster_size = "w342"):
    base_url = "https://image.tmdb.org/t/p/"
    poster_url = f"{base_url}{poster_size}/{poster_api_path}"
    return poster_url

#def get_movies(how_many):
#    data = get_popular_movies()
#    return data["results"][:how_many]

def get_movies(list_type, how_many):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    print(response.json())
    return response.json()["cast"]

def get_single_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()