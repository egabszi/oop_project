# van egy listán, amiben .mkv file-ok vannak
# ezekhez a file-okhoz akarunk letölteni 
    # képeket -> pipa
    # szöveges állományt -> json -> pipa
    # még egyéb metaadatokat
    # a képeket egy posters nevű mappába kiírni
    # a json-öket kiírni egy meta_data mappába
    # ha mégiscsak a listában van az elem, akkor próbáljuk megtalálni a megfelelőt

# később refakotorálnoi fogjuk a kódot: python loggert fogunk használni

import os
import tmdbsimple as tmdb
from urllib.request import urlopen
import sys
if __name__ == '__main__':
    import file_handler
else:
    from . import file_handler

class Search:
    tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'
    image_path_string = 'https://image.tmdb.org/t/p/original'
    backdrop_path_string = 'https://image.tmdb.org/t/p/original'

    def __init__(self):
        self.file_handler = file_handler.FileHandler()
        self.movie_name = None

    # setter és getter megoldásra fogjuk majd cserélni
    def get_json_data(self, movie_name):
        self.movie_name = movie_name
        if not movie_name:
            raise Exception("Nem adtál meg film címet, kérlek pótold")
        try:
            search = tmdb.Search()
            response = search.movie(query=movie_name)['results']

        except Exception as e:
            return False, str(e)

        return response[0] if response else False

    def _get_poster_link(self, data):
        return f"{self.image_path_string}{data['poster_path']}"
        
    def write_image(self, data):
        if not data:
            return False, "There is no data"

        poster_link = self._get_poster_link(data)
        poster_path = os.path.join(self.file_handler.poster_folder, self.movie_name + '.jpg')

        try:
            with open(poster_path, "wb") as poster:
                poster.write(urlopen(poster_link).read())
        except Exception as e:
            return False, str(e)

        return poster_path

    def write_meta_data(self, data):
        if not os.path.exists(self.file_handler.meta_data_folder):
            return False, f"The given {self.file_handler.meta_data_folder} folder does not exists"

        file_path = os.path.join(self.file_handler.meta_data_folder, self.movie_name + '.json')

        data['poster_location'] = os.path.join(self.file_handler.poster_folder, self.movie_name + '.jpg')
        data['data_location'] = os.path.join(self.file_handler.folder_path, self.movie_name + '.mkv')
        return self.file_handler.write_file(file_path, data)

if __name__ == '__main__':
    test = Search()

    movie_name = 'Braveheart'

    movies = [movie[:-4] for movie in os.listdir(r"D:\oop_project\movies") if '.mkv' in movie]
    print(movies)
    for item in movies:
        data = test.get_json_data(item)
        test.write_meta_data(data)

        if not data:
            print(f"error at query data from api: {data}")
            exit()

        test.write_image(data)
    

