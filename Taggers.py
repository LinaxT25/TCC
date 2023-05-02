import psycopg2

def tagger(connection, userid):
    try:
        cursor = connection.cursor()

        print("Searching if user made tags for repository...")
        query = 'SELECT tagger FROM "dv8fromtheworld/jda".tags ' + "WHERE tagger ->> 'user' = %s"
        cursor.execute(query, (userid,))
        data = cursor.fetchall() #returns a list of tuples

        if len(data) != 0:
            print("User made tags for repository.\n")
            cursor.close()
            extractedData = []
            for tuples in data:
                extractedData.append(tuples[0].get('date'))
            return tuple(("Taggers", tuple(extractedData)))
        else:
            print("User don't made tags for repository.\n")
            cursor.close()
            return tuple(("Taggers", None))
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)