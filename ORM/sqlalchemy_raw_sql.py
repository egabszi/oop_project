# CRUD - Create, Read, Update, Delete

from sqlalchemy import create_engine

engine = create_engine('sqlite:///movies.db', echo = True)