import requests

from common_utils.variables import API_KEY


def getMovieCredits(movie_id, language='en-US'):
    if not movie_id:
        return 'Missing movie ID'

    parameters = {'api_key': API_KEY, 'language': language}
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getRecommendations(movie_id, language='en-US', page=1):
    if not movie_id:
        return 'Missing movie ID'

    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getSimilarMovies(movie_id, language='en-US', page=1):
    if not movie_id:
        return 'Missing movie ID'

    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/similar'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getPopularMovies(language='en-US', page=1):
    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = f'https://api.themoviedb.org/3/movie/popular'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getUpcomingMovies(language='en-US', page=1):
    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = f'https://api.themoviedb.org/3/movie/upcoming'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getMovieDetails(movie_id, language='en-US'):
    if not movie_id:
        return 'Missing movie ID'

    parameters = {'api_key': API_KEY, 'language': language}
    url = f'https://api.themoviedb.org/3/movie/{movie_id}'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getMovieLatest(language='en-US'):
    parameters = {'api_key': API_KEY, 'language': language}
    url = 'https://api.themoviedb.org/3/movie/latest'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getMovieTopRated(language='en-US', page=1):
    parameters = {'api_key': API_KEY, 'language': language, 'page': page}
    url = 'https://api.themoviedb.org/3/movie/top_rated'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results


def getMovieDiscover(language='en-US', sort_by='popularity.desc', page=1, vote_average=5, vote_sort='gte', with_genres=''):
    parameters = {'api_key': API_KEY, 'language': language,
                  'page': page, 'sort_by': sort_by, f'vote_average.{vote_sort}': vote_average, 'with_genres': with_genres}
    url = 'https://api.themoviedb.org/3/discover/movie'

    res = requests.get(url, params=parameters)
    results = res.json()

    return results



