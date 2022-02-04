import mysql.connector
import data_extraction
from mysql.connector import Error

res = []

def create_connection_ensembl():
    connection = None
    try:
        connection = mysql.connector.connect(host='ensembldb.ensembl.org', user='anonymous', port='5306')
        print("Connection successfull")
        execute_query(connection, "USE takifugu_rubripes_core_105_12")
    except Error as e:
        print("Error while connecting :", e)
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    result=()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
    except Error as e:
        print("Error while executing query: ", e)
    return result

def save_queryresult(results):
    for x in results:
        res.append(x)

def create_connection_own():
    connection = None
    try:
        connection = mysql.connector.connect(host='localhost', user='root', password='Rieke1999', db='interleukine', auth_plugin='caching_sha2_password')
        print("Connection successfull")
    except Error as e:
        print("Error while connecting :", e)
    return connection

