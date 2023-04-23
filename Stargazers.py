import psycopg2

def starredUser(connection, user):
    try:
        cursor = connection.cursor()

        print("Searching if user starred a repository...")
        cursor.execute('SELECT starred_at FROM "dv8fromtheworld/jda".stargazers WHERE "user" = %s;', (user,))
        data = cursor.fetchall()#returns a list of tuples
        #print(data)

        if len(data) != 0:
            print("User starred the repository.\n")
            cursor.close()
            return tuple(["Starred", data])
        else:
            print("User not starred the repository.\n")
            cursor.close()
            return None
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
