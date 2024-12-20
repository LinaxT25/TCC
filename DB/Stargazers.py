import psycopg2


def starred_user(connection, userid):
    try:
        cursor = connection.cursor()

        print("Searching if user starred a repository...")
        cursor.execute('SELECT starred_at FROM "dv8fromtheworld/jda".stargazers WHERE "user" = %s;', (userid,))
        data = cursor.fetchall()  # returns a list of tuples

        if len(data) != 0:
            print("User starred the repository.\n")
            cursor.close()
            extracted_data = []
            for tuples in data:
                extracted_data.append(tuples[0])
            return tuple(("Starred", tuple(extracted_data)))
        else:
            print("User not starred the repository.\n")
            cursor.close()
            return tuple(("Starred", None))
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
