# fel kell olvasni az mkv file-okat a mappából / mappákból
# kiírni a szöveges metaadatot
# ki kell írni a képeket - itt oldjuk meg, vagy a lekérés osztályánál
# törölni a képeket
# törölni a metaadatot

#mi van akkor, ha hiányzik, törölted a filmet
# metaadat hiányzik
# poster hiányzik

# file alapú

# adatbázis kezelés:

# MongoDB - NoSQL
# Compass

# jelenleg 1 mappából tudunk csak filmet felolvasi, azt szeretnénk, hogy képes legyen megoldás
# több mappa egyidejű kezelésére - > mappákat lehessen törölni, hozzáadni
# többszálasítás- lehetőségek- kell e - > itt elméleti szinten a következekőket kell megemlíteni:
# thread- multiprocessing - > multiprocessing - > GIL (Global Interpreter Lock)
# statisztikák: pl. hány filmem van, metaadatokból mit lehet - opcionális
# statisztikákhoz plot - ennél a feladatnál opcionális (matplotlib, seaborn, scatterplot)


##############################################
# postgres - minimális sql
# pandas - yml,  csv, ini, xml - numpy
# ORM - Object Relational Mapping -> miért nem szeretem, miért szeretik mások, miért nem szeretik az adatbázis közeli emberek

# postgres- adatbázis driver, nativ sql futtatások

# rest api - 

# UI-os projekt
# plot
# folyamat figyelés - töltő monitoring
# minimális docker - basics: mi a docker; hogyan lehet futtatni, leállítani; logokat ellenőrizni; docket compose mint orchestrator- alapjai
# adatbetöltések



import os
import json


class FileHandler:
    folder_path = r"D:\oop_project\movies"

    poster_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)),'posters')
    meta_data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)),'meta_data')

    #def __init__(self, folder_path: str):
    def __init__(self):
        self._create_necessary_folders()
        #self.folder_path = folder_path

    def _create_necessary_folders(self):
        if not os.path.exists(self.poster_folder):
            os.mkdir(self.poster_folder)
        if not os.path.exists(self.meta_data_folder):
            os.mkdir(self.meta_data_folder)

    def delete_file(self, file_path):
        try:
            os.remove(file_path)
        except FileNotFoundError:        
            return False, 'File nem található!'
        except Exception as e:
            return False, str(e)

        return True

    def write_file(self, file_path, data):
        if data:
            # a data-t át tudjuk e alakítani json-é           
            try: 
                json.dumps(dict(data))
            except TypeError:
                return False, 'Nem jó adattípust adtál meg.'
            except Exception as e:
                return False, str(e)

            if isinstance(file_path, str):        
                with open(file_path, 'w', encoding='utf-8') as json_file:
                    json.dump(data, json_file)
            else:
                return False, 'Nem string'
        else:
            return False, 'Nem adtál meg adatokat a kiíráshoz'

        return True

    def get_movie_list(self):
        if not os.path.exists(self.folder_path):
            return False, "The given path is not exists"
        
        return [file[0:-4] for file in os.listdir(self.folder_path) if file[-3:] in ('mkv')]

    def get_meta_data_list(self):
        return [meta[:-5] for meta in os.listdir(self.meta_data_folder)]

    def get_poster_list(self):
        return [poster[:-4] for poster in os.listdir(self.poster_folder)]

    def get_diff(self):
        #refaktoráljuk majd azt, hogy ne a get_list
        # van metaadat de nincs poster
        meta_data_list = self.get_meta_data_list()
        poster_list = self.get_poster_list()
        movie_list= self.get_movie_list()

        # nincs file, de van metaadat
        need_to_delete_meta = [meta for meta in meta_data_list if meta not in movie_list]
        # nincs file, de van poster
        need_to_delete_poster = [poster for poster in poster_list if poster not in movie_list]

        need_to_download_meta = [movie for movie in movie_list if movie not in meta_data_list]
        need_to_download_poster = [movie for movie in movie_list if movie not in poster_list]

        return {
                "need_to_delete_meta":need_to_delete_meta,
                "need_to_delete_poster": need_to_delete_poster,
                "need_to_download_meta": need_to_download_meta,
                "need_to_download_poster": need_to_download_poster}
        

class FileHandler2(FileHandler):
    def __init__(self):
        super().__init__()

    def write_file(self, file_path, data):
        with open(file_path, 'w') as file:
            file.write(data)
        return True

    @classmethod
    def first_cls(cls):
        return cls()

    @staticmethod
    def first_static(number):
        return number ** 2



if __name__ == '__main__':
    folder_path = r"D:\oop_project\movies"
    handler = FileHandler()

    # print(handler.get_list())

    # handler.write_file("test.json", {"kulcs": "érték"})
    # handler.delete_file("test.json")

    #handler_2 = FileHandler2()
    #print(handler_2.get_list())

    #handler_2.write_file("test.txt", "Nagyon jó ez az oop")

    #print(FileHandler2().first_cls())

    #print(FileHandler2().first_static(5))

    print(handler.get_meta_data_list())
    print(handler.get_poster_list())
    print(handler.get_diff())
    # print(handler.get_movie_list())



    #sikerült a github