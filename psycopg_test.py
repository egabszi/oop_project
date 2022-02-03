import psycopg2 as postgres

connection = postgres.connect(
                                user="postgres",
                                password="postgres",
                                host="localhost",
                                port=5432,
                                database="postgres"
                                )
connection.autocommit = False

cursor = connection.cursor()
temp = cursor.execute("select * from car")

#print(cursor.fetchone())

data = cursor.fetchall()


table = "test_car"
insert_statement = f"""
    insert into {table} (car_id, name, color, motor_type) values (%s, %s, %s, %s)
"""

test_car_data = [
    (5, "Ferrari", "piros", "benzin"), 
    (6, "Szengjong", "csont", "elektromos"), 
    (7, "Trabant", "kék", "benzines")
]

#cursor.callproc('Function_name',[IN and OUT parameters,]) 
# cur.execute("CALL sales(%s, %s);", (val1, val2))

cursor.executemany(insert_statement, test_car_data)

cursor.execute("ide írod a tárolt eljárás nevét")
connection.commit()

cursor.close()
connection.close()