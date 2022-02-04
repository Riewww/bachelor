import mysql.connector

from mysql.connector import Error


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
query = "SELECT dna.seq_region_id, dna.sequence, gene.seq_region_start, gene.seq_region_end FROM dna INNER JOIN " \
        "(SELECT gene_id, description, gene.seq_region_id, seq_region_start, seq_region_end FROM gene WHERE description LIKE \"%interleukin%\") gene " \
        "WHERE gene.seq_region_id = dna.seq_region_id"


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





id = []
seq = []
seqcut = []
start = []
end = []



def split_results(result):
    for x in result:
        a, b, c, d = x
        id.append(str(a))
        seq.append(b)
        start.append(c)
        end.append(d)

def cut_sequence(seq,start,end):
    i = 1
    for x in seq:
        seqcut.append(str(x)[int(str(start[i])):int(str(end[i]))])
        i+1
    return seqcut

split_results(res)
cut_sequence(seq,start,end)



con = create_connection2()
cur = con.cursor()
for x in id:
    i=1
    querys= "INSERT INTO takifugu (id,seq) VALUES (" + str(x) + ",\" " + str(seqcut[i]) + "\"); "
    i+1
    cur.execute(querys)
    con.commit()
    cur.fetchall()

