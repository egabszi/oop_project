import os
import json
from utils. file_handler import FileHandler
from utils.search import Search


def download_metadata():
    # ha nincsenek metaadatok akkor töltsük le őket
    search = Search()

    diff = search.file_handler.get_diff()
    print(diff)
#egy looppal megoldani a letöltéseket, akkor töltsük le őket
    if diff['need_to_delete_poster']:
        for item in diff['need_to_delete_poster']:
            file_path = os.path.join(search.file_handler.poster_folder, item + '.jpg')
            search.file_handler.delete_file(file_path)

    if diff['need_to_delete_meta']:
        for item in diff['need_to_delete_meta']:
            file_path = os.path.join(search.file_handler.meta_data_folder, item + '.json')
            search.file_handler.delete_file(file_path)

    if diff["need_to_download_meta"]:
        for item in diff["need_to_download_meta"]:
            data = search.get_json_data(item)
            search.write_meta_data(data)


    if diff["need_to_download_poster"]:
        for item in diff["need_to_download_poster"]:
            data_file = [os.path.join(search.file_handler.meta_data_folder,file)\
                         for file in os.listdir(search.file_handler.meta_data_folder)if item in file]

            data = None
            if data_file:
                with open(data_file[0], 'r') as json_file:
                    data = json.load(json_file)

                search.movie_name = item
                search.write_image(data)


    
    # movies = [movie[:-4] for movie in os.listdir(r"D:\oop_project\movies") if '.mkv' in movie]
    # print(movies)
    # for item in movies:
    #     data = search.get_json_data(item)
    #     search.write_meta_data(data)

    #     if not data:
    #         print(f"error at query data from api: {data}")
    #         exit()

    #     search.write_image(data)


    # pass




if __name__ == '__main__':
    download_metadata()