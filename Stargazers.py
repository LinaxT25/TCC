import psycopg2

def starredUser(connection, user):
    try:
        cursor = connection.cursor()
        print("Searching if user starred a repository...")

        cursor.execute('SELECT * FROM "dv8fromtheworld/jda".stargazers WHERE "user" = %s;', (user,))

        data = cursor.fetchall()
        #print(data)

        if len(data) != 0:
            print("User starred the repository.\n")
            cursor.close()
            return list(map(lambda x: ("starred", x[2]), data))
        else:
            print("User not starred the repository.\n")
            cursor.close()
            return None
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
