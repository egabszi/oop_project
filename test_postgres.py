import os
import json
import datetime

file_location = r"D:\oop_project\meta_data\Aladdin.json"

# JSON file struktúrájából ey create table utasítás:
# tipusosítás dinamikus megoldása

data = None
with open (file_location, "r") as f:
    data = json.load(f)

print(data)


cols = {}
cols_type = None

for key, value in data.items():
    if isinstance(value, float):
        cols_type = 'decimal({precision}, 1)'.format(precision=len(str(value).split(".")[0]))
    elif isinstance(value, int) and (value not in (True, False)):
        cols_type = 'int' #bigint
    elif isinstance(value, datetime.date):
        cols_type = 'date'
    elif value in (True, False):
        cols_type = 'boolean'
    else:
        # genre id-t refaktor során le kell majd tárolni -> új tábla, many-to-many kapcsolat
        cols_type = 'varchar({precision})'.format(precision=len(value))

    try:
        dto = datetime.datetime.strptime(value, '%Y-%m-%d').date()
        cols_type = 'date'
    except:
        pass

    cols[key] = cols_type

del cols['genre_ids']

print(cols)

create_table_statement = 'create table stage_data ('

for key, val in cols.items():
    create_table_statement += f"{key} {val},"

create_table_statement += 'creation_date date default now())'
print(create_table_statement)


    

