#!/usr/bin/python3
"""[a script that lists all states from the database hbtn_0e_0_usa]
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
    c.execute("""SELECT * FROM states ORDER BY id""")
    row = c.fetchall()
    for i in row:
        print(i)
    c.close()
    db.close()
