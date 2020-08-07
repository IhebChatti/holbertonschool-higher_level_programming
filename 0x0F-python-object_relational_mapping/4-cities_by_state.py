#!/usr/bin/python3
"""[a script that lists all cities from the database hbtn_0e_4_usa]
"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    username = args[1]
    password = args[2]
    dbname = args[3]
    db = MySQLdb.connect("localhost", username, password, dbname, 3306)
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name FROM cities INNER JOIN
              states ON cities.state_id = states.id ORDER BY id ASC""")
    row = c.fetchall()
    for i in row:
        print(i)
    c.close()
    db.close()
