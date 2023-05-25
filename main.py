from BD import Close, Connect, User
import DataSorting
import DataExport

if __name__ == '__main__':

    print("Select the type of data extraction:")
    print("[1] Input the user ID.")
    print("[2] Extract for all users.")

    option = input()

    if option == '1':
        print("Input the user ID:")
        userID = input()

        connection = Connect.connect()
        user = User.retrieveActor(connection, userID)

        if user is not False:
            print("User found!\n")
            temporalTuple = DataSorting.sorting(connection, userID)

            DataExport.exportToCsv(temporalTuple, userID)
        else:
            print("User not found!\n")

        Close.closeConnection(connection)

    elif option == '2':

        connection = Connect.connect()
        userList = User.retrieveActors(connection)

        if userList is not False:
            print("List of users found!\n")

            for user in userList:
                temporalTuple = DataSorting.sorting(connection, user[0])

                DataExport.exportToCsv(temporalTuple, user[0])
        else:
            print("User not found!\n")

        Close.closeConnection(connection)

    else:
        print("Error in selection!")

