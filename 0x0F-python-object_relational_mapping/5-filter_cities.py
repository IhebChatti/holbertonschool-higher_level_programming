#!/usr/bin/python3
"""[a script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa]
"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    username = args[1]
    password = args[2]
    dbname = args[3]
    statename = args[4]
    db = MySQLdb.connect("localhost", username, password, dbname, 3306)
    c = db.cursor()
    c.execute("""SELECT cities.name FROM cities WHERE state_id = (SELECT
              id FROM states WHERE name='%s')""" % statename)
    rows = c.fetchall()
    print(", ".join(i[0] for i in rows))
    c.close()
    db.close()
