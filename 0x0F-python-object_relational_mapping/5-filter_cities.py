#!/usr/bin/python3
""" takes in the name of a state as an argument and lists all cities """
import MySQLdb
import sys


if __name__ == "__main__":
    usrinpt = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("""SELECT cities.name FROM
            cities INNER JOIN states ON states.id=cities.state_id
            WHERE states.name=%s""", (usrinpt,))

    rows = cur.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")

    cur.close()
    db.close()
