import tmdbsimple as tmdb
from urllib.request import urlopen

tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'
image_path_string = 'https://image.tmdb.org/t/p/original'
backdrop_path_string = 'https://image.tmdb.org/t/p/original'

# poster_path

search = tmdb.Search()
response = search.movie(query="Alien")['results'][0]

print(response)

poster_link = f"{image_path_string}{response['poster_path']}" 

with open("Alien.jpg", "wb") as poster:
    poster.write(urlopen(poster_link).read())

def test_func(*args, **kwargs):
    if kwargs.get('alma'):
        # do somethin
        pass
    if kwargs.get('valami'):
        pass


test_func(1,2,3)

test_func(1,2,3,4,5,6,67,7,8, alma="piros")
test_func(1,2,3,4,5,6,67,7,8,352352)