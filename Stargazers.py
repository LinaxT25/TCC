import itertools

import psycopg2

def starredUser(connection, userid):
    try:
        cursor = connection.cursor()

        print("Searching if user starred a repository...")
        cursor.execute('SELECT starred_at FROM "dv8fromtheworld/jda".stargazers WHERE "user" = %s;', (userid,))
        data = cursor.fetchall() #returns a list of tuples
        #print(data)

        if len(data) != 0:
            print("User starred the repository.\n")
            cursor.close()
            extractedData = []
            for tuples in data:
                extractedData.append(tuples[0])
            return tuple(("Starred", tuple(extractedData)))
        else:
            print("User not starred the repository.\n")
            cursor.close()
            return tuple(("Starred", None))
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
