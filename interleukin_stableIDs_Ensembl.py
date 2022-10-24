#import data_extraction
import database



#query getting region id, sequence, start and end of sequence from genes where the word interleukin is in the description
# old query_ensembl =  "SELECT gene.stable_id, dna.sequence, gene.seq_region_start, gene.seq_region_end, gene.description FROM dna INNER JOIN " \
       # "(SELECT gene_id, description, gene.seq_region_id, seq_region_start, seq_region_end, gene.stable_id FROM gene WHERE description LIKE \"%interleukin%\") gene " \
        #"WHERE gene.seq_region_id = dna.seq_region_id"
query_ensembl = "SELECT stable_id FROM gene WHERE description LIKE \"%interleukin%\" "


database.save_queryresult(database.execute_query(database.create_connection_ensembl(), query_ensembl))
#data_extraction.split_results(database.res)
#data_extraction.cut_sequence(data_extraction.seq, data_extraction.start, data_extraction.end)


connection_own = database.create_connection_own()
connection_own_cursor = connection_own.cursor()

#inserts seq id and cut sequence into to own database
#i = 0
for x in database.res:
    query_own = "INSERT INTO takifugu_rubripes (id) VALUES (\"" + x + "\"); "
    #i = i+1
    connection_own_cursor.execute(query_own)
    connection_own.commit()
    connection_own_cursor.fetchall()


