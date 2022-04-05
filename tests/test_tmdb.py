import pytest

import tmdb_client
from tmdb_client import *
from unittest.mock import Mock
from main import app

'''
def test_mocking(monkeypatch):
   my_mock = Mock
   my_mock.return_value = 2
   monkeypatch.setatter("tests.test_tmdb.some_function_to_mock", my_mock)
   result = some_function_to_mock()
   assert result == 2
def test_get_poster_url_uses_default_size():
    # Przygotowanie danych
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    # Wywołanie kodu, który testujemy
    poster_url = get_poster_url(poster_api_path=poster_api_path)
    # Porównanie wyników
    assert expected_default_size in poster_url
def test_get_movies_list_type_popular():
    movies_list = get_movie_library(list_type="popular")
    assert movies_list is not None
def test_get_movies_library(monkeypatch):
    # Lista , którą będzie zwracać przysłonięte "zapytanie do Api"
    mock_movie_list = ['Movie1', 'Movie2']
    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    response = requests_mock.return_value
    # Przesłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_movie_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movies_list = tmdb_client.get_movie_library(list_type="popular")
    assert movies_list == mock_movie_list
'''

def test_get_single_movie(monkeypatch):
   mock_single_movie_url = "URL"

   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie_url
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   single_movie = tmdb_client.get_single_movie('379686')
   assert single_movie == mock_single_movie_url


def test_get_movie_images(monkeypatch):
   mock_movie_image = "URL"

   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movie_image
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movie_image = tmdb_client.get_single_movie('379686')
   assert movie_image == mock_movie_image


def test_single_movie_cast(monkeypatch):
   mock_single_movie_cast = "URL"

   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie_cast
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movie_cast = tmdb_client.get_single_movie('379686')
   assert movie_cast == mock_single_movie_cast


@pytest.mark.parametrize('list_type, result',(
        ('popular', 'movie/popular'),
        ('top_rated', 'movie/top_rated'),
        ('upcoming', 'movie/upcoming')
))
def test_homepage(monkeypatch,list_type, result):
    api_mock = Mock(return_value={"results": []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert get_single_movie(list_type) == call_tmdb_api(result)
