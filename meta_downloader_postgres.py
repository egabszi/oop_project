import os
from utils.search import Search
from utils.postgres_handler import PostgresHandler

def etl_for_movies(need_to_create):
    search = Search()
    db = PostgresHandler()

    if need_to_create:
        db.create_database_objects()
        db.etl_log("create_database_objects", 'OK')
    
    folder_movies = search.file_handler.get_movie_list()
    all_movie_data = db.get_all_movies()

    db_movies = [item['searched_name'] for item in all_movie_data]

    diff = [item for item in folder_movies if item not in db_movies]

    if diff:
        for movie in diff:
            data = search.get_json_data(movie)
            poster_path = search.write_image(data)

            params = (data['id'], movie, data['original_title'])
            movie_id = db.insert_movie(params)
            
            del data['genre_ids']
            del data['id']

            data['poster_folder_path'] = poster_path
            data['movie_folder_path'] = os.path.join(search.file_handler.folder_path, movie + '.mkv')

            # *args, **kwargs

            # függvényeknek tudunk tetszőleges mennyiségű, (nem előre definiált)
            # bejövő paramétert -> *args , -> packing és unpacking
            #print(*data.keys())

            params = (movie_id, *data.values())

            db.insert_meta(params)
        db.etl_log('if diff: download ', 'OK')
    else:
        
        for item in all_movie_data:
            if not os.path.exists(item['movie_folder_path']):
                search.file_handler.delete_file(item['poster_folder_path'])
                db.delete_record(item['searched_name'])
            
            else:
                if not os.path.exists(item['poster_folder_path']):
                    search.movie_name = item['searched_name']
                    search.write_image(item)

        db.etl_log('if not diff: download or delete ', 'OK')

if __name__ == "__main__":
    # ha True -> akkor eldob minden objektumot, és újra lérehozza => ősfeltöltés
    # ha False -> akkor nem nyúl az objektumokhoz és az ellenőrzéseket elvégzi
    etl_for_movies(False)

