import psycopg2

def reactedUser(connection, userid):
    try:
        cursor = connection.cursor()

        print("Searching if user reacted a repository...")
        cursor.execute('SELECT created_at FROM "dv8fromtheworld/jda".reactions WHERE "user" = %s;', (userid,))
        data = cursor.fetchall() #returns a list of tuples
        #print(data)

        if len(data) != 0:
            print("User reacted the repository.\n")
            cursor.close()
            extractedData = []
            for tuples in data:
                extractedData.append(tuples[0])
            return tuple(("Reactions", tuple(extractedData)))
        else:
            print("User not reacted the repository.\n")
            cursor.close()
            return tuple(("Reactions", None))
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
