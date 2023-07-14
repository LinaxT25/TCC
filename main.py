from BD import Close, Connect, User
from FP_Growth import FPGrowth
import DataSorting
import DataExport
from UI import UI

if __name__ == '__main__':
    # UI.callGui()

    print("Select the type of data extraction:")
    print("[1] Input the user ID.")
    print("[2] Extract for all users.")

    option = input()

    if option == '1':
        print("Input the user ID:")
        userID = input()

        connection = Connect.connect()
        user = User.retrieveActor(connection, userID)

        #TODO Check if user already exists in database
        if user is not False:
            print("User found!\n")

            temporalTuple = DataSorting.sorting(connection, userID)

            DataExport.exportToCsv(temporalTuple, userID)
            DataExport.exportToDB(temporalTuple, userID, connection)
        else:
            print("User not found!\n")

        Close.closeConnection(connection)

    elif option == '2':

        connection = Connect.connect()
        userList = User.retrieveActors(connection)

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

                DataExport.exportToCsv(temporalTuple, user[0])
                DataExport.exportToDB(temporalTuple, user[0], connection)
        else:
            print("User not found!\n")

        Close.closeConnection(connection)

    elif option == '3':
        FPGrowth.dataPattern()

    else:
        print("Error in selection!")

