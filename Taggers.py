import psycopg2

def tagger(connection, id):
    try:
        cursor = connection.cursor()
        print("Searching if user made tags for repository...")

        query = 'SELECT * FROM "dv8fromtheworld/jda".tags ' + "WHERE tagger ->> 'user' = %s"

        cursor.execute(query, (id,))

        data = cursor.fetchall()

        if len(data) != 0:
            print("User made tags for repository.\n")
            cursor.close()
            return True
        else:
            print("User don't made tags for repository.\n")
            cursor.close()
            return False
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)