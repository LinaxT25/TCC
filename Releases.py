import psycopg2

def releaseUser(connection, user):
    try:
        cursor = connection.cursor()
        print("Searching if user make a release for repository...")

        cursor.execute('SELECT created_at FROM "dv8fromtheworld/jda".releases WHERE "author" = %s;', (user,))

        data = cursor.fetchall()
        #print(data)

        if len(data) != 0:
            print("User made a release for repository.\n")
            cursor.close()
            return tuple(["Releases", data])
        else:
            print("User don't made a release for repository.\n")
            cursor.close()
            return None
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)