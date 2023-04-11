#!/usr/bin/python3

"""
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
(Safe from SQL Injection)
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":

    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = con.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name ='{:s}' ORDER BY id ASC;".format(argv[4]))
    db = cursor.fetchall()
    for i in db:
        print(i)

    cursor.close()
    con.close()
