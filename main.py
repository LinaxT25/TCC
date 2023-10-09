from DB import Close, Connect, User
from FP_Growth import PatternAnalysis
from Export import DataExport, DataSorting

if __name__ == '__main__':

    print("Select the option desired:")
    print("[1] Input the user ID.")
    print("[2] Extract for all users.")
    print("[3] Analyze data patterns from standard table in database.")

    option = input()

    if option == '1':
        print("Input the user ID:")
        userID = input()

        connection = Connect.connect()
        user = User.retrieve_actor(connection, userID)

        # TODO Check if user already exists in database
        if user is not False:
            print("User found!\n")

            temporalTuple = DataSorting.sorting(connection, userID)

            DataExport.export_to_csv(temporalTuple, userID)
            DataExport.export_to_db(temporalTuple, userID, connection)
        else:
            print("User not found!\n")

        Close.close_connection(connection)

    elif option == '2':

        connection = Connect.connect()
        userList = User.retrieve_actors(connection)

        if userList is not False:
            print("List of users found!\n")

            # Check if table exists in database to export
            cursor = connection.cursor()
            cursor.execute('select exists(select * from information_schema.tables where table_name=%s)',
                           ('standard',))
            # Then delete for insert new data
            if cursor.fetchone()[0] is True:
                delete = 'DROP TABLE "dv8fromtheworld/jda".standard;'
                cursor.execute(delete)
                connection.commit()
                cursor.close()

            for user in userList:
                temporalTuple = DataSorting.sorting(connection, user[0])

                DataExport.export_to_csv(temporalTuple, user[0])
                DataExport.export_to_db(temporalTuple, user[0], connection)
        else:
            print("User not found!\n")

        Close.close_connection(connection)

    elif option == '3':
        PatternAnalysis.fp_growth()
    else:
        print("Error in selection!")

