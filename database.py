import mysql.connector
from mysql.connector import Error
from typing import List


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(host='ensembldb.ensembl.org', user='anonymous', port='5306')
        print("Connection successfull")

    except Error as e:
        print("Error while connecting :", e)

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute("USE takifugu_rubripes_core_105_12")
        cursor.close()
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

    except Error as e:
        print("Error while executing query: ", e)

    return result


connection = create_connection()
query = "SELECT gene_id, seq_region_id, description FROM gene WHERE description LIKE '%interleukin%'"

res = []

for x in execute_query(connection,query):
    res.append(x)

def create_connection2():
    connection = None
    try:
        connection = mysql.connector.connect(host='localhost', user='root', password='Rieke1999', db='interleukine', auth_plugin='caching_sha2_password')
        print("Connection successfull")

    except Error as e:
        print("Error while connecting :", e)

    return connection


con = create_connection2()
cur = con.cursor()
for x in res:
    querys= "INSERT INTO more (eins,zwei,drei) VALUES " + str(x) + "; "
    cur.execute(querys)
    con.commit()
    cur.fetchall()

