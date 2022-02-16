import mysql.connector
from mysql.connector import Error

res = []

#creates a connection to ensembl database
def create_connection_ensembl():
    connection = None
    try:
        connection = mysql.connector.connect(host='ensembldb.ensembl.org', user='anonymous', port='5306')
        print("Connection successfull")
        execute_query(connection, "USE gasterosteus_aculeatus_core_105_1")
    except Error as e:
        print("Error while connecting :", e)
    return connection

#executing query
def execute_query(connection, query):
    cursor = connection.cursor()
    result = ()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
    except Error as e:
        print("Error while executing query: ", e)
    return result

#saves results from executed query in res
def save_queryresult(results):
    for x in results:
        res.append(''.join(filter(str.isalnum, str(x))))

#creates connection to own database
def create_connection_own():
    connection = None
    try:
        connection = mysql.connector.connect(host='localhost', user='root', password='Rieke1999', db='interleukine', auth_plugin='caching_sha2_password')
        print("Connection successfull")
    except Error as e:
        print("Error while connecting :", e)
    return connection

