import psycopg2


def reacted_user(connection, userid):
    try:
        cursor = connection.cursor()

        print("Searching if user reacted a repository...")
        cursor.execute('SELECT created_at FROM "dv8fromtheworld/jda".reactions WHERE "user" = %s;', (userid,))
        data = cursor.fetchall()  # returns a list of tuples

        if len(data) != 0:
            print("User reacted the repository.\n")
            cursor.close()
            extracted_data = []
            for tuples in data:
                extracted_data.append(tuples[0])
            return tuple(("Reactions", tuple(extracted_data)))
        else:
            print("User not reacted the repository.\n")
            cursor.close()
            return tuple(("Reactions", None))
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
