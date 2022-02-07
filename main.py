import data_extraction
import database

#query getting region id, sequence, start and end of sequence from genes where the word interleukin is in the description
query_ensembl = "SELECT dna.seq_region_id, dna.sequence, gene.seq_region_start, gene.seq_region_end FROM dna INNER JOIN " \
        "(SELECT gene_id, description, gene.seq_region_id, seq_region_start, seq_region_end FROM gene WHERE description LIKE \"%interleukin%\") gene " \
        "WHERE gene.seq_region_id = dna.seq_region_id"


database.save_queryresult(database.execute_query(database.create_connection_ensembl(), query_ensembl))
data_extraction.split_results(database.res)
data_extraction.cut_sequence(data_extraction.seq, data_extraction.start, data_extraction.end)


connection_own = database.create_connection_own()
connection_own_cursor = connection_own.cursor()

#inserts seq id and cut sequence into to own database
for x in data_extraction.id:
    i = 1
    query_own = "INSERT INTO takifugu (id,seq) VALUES (" + str(x) + ",\" " + str((data_extraction.seqcut)[i]) + "\"); "
    i = i+1
    connection_own_cursor.execute(query_own)
    connection_own.commit()
    connection_own_cursor.fetchall()


