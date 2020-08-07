#!/usr/bin/python3
"""[a script that takes in arguments and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument.
    But this time, itis safe from MySQL injections!]
"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    username = args[1]
    password = args[2]
    dbname = args[3]
    name = args[4]
    db = MySQLdb.connect("localhost", username, password, dbname, 3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name = '%s'""" % (name))
    row = c.fetchall()
    for i in row:
        print(i)
    c.close()
    db.close()
