# ---- Homework 'Creating Tables' ---- #

import sqlite3

# create databasae 'cars'
db = sqlite3.connect('cars')

# create cursor
cursor = db.cursor()

# create table 
cursor.execute("""CREATE TABLE inventory
                (Make TEXT, Model TEXT, Quantity INT)
                """)

# close database
db.close()