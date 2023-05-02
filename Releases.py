import psycopg2

def releaseUser(connection, userid):
    try:
        cursor = connection.cursor()

        print("Searching if user make a release for repository...")
        cursor.execute('SELECT created_at FROM "dv8fromtheworld/jda".releases WHERE "author" = %s;', (userid,))
        data = cursor.fetchall() #returns a list of tuples
        #print(data)

        if len(data) != 0:
            print("User made a release for repository.\n")
            cursor.close()
            extractedData = []
            for tuples in data:
                extractedData.append(tuples[0])
            return tuple(("Releases", tuple(extractedData)))
        else:
            print("User don't made a release for repository.\n")
            cursor.close()
            return tuple(("Releases", None))
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)