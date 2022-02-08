import database

path = ""


def write_file(path, header, sequence):
    f = open(path, 'w')
    for x in header:
        f.write(header + '\n' + sequence + '\n \n')


connection = database.create_connection_own()
database.save_queryresult(database.execute_query(connection, "SELECT id, seq FROM takifugu_rubripes"))

for x in database.res:
    header, sequence = str(x)