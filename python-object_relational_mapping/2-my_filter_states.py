#!/usr/bin/python3
"""connect database."""

import MySQLdb
import sys


def connect_database_1(usr, paswd, dt_name, st_name):
    """connects withdatabase to gather information.
    """

    db = MySQLdb.connect(host='localhost', user=usr, passwd=paswd,
                         db=dt_name, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE  name = '{}' ORDER BY id ASC"
                .format(st_name))
    res = cur.fetchall()
    for state in res:
        if state[1] == st_name:
            print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    """ Exectues if
    main is calling it"""
    try:
        if sys.argv[4]:
            connect_database_1(
                sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    except MySQLdb.Error:
        pass
