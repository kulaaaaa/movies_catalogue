from flask import Flask, render_template, request
import tmdb_client
import random



app = Flask(__name__)

@app.route('/')
def homepage():
    movie_lists = ["now_playing", "popular", "top_rated", "upcoming"]
    selected_list = request.args.get('list_type',"popular")
    if selected_list not in movie_lists:
        selected_list = "popular"         
    movies = tmdb_client.get_movies(how_many=6, list_type=selected_list)
    return render_template("homepage.html", movies=movies, movie_lists=movie_lists, list_type=selected_list)

@app.context_processor
def utility_processor():
    def tmdb_image_url(poster_api_path, poster_size):
        return tmdb_client.get_poster_url(poster_api_path, poster_size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    b_images = tmdb_client.get_single_movie_images(movie_id)
    b_image = random.choice(b_images['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast, b_image=b_image)

if __name__ == '__main__':
    app.run(debug=True)