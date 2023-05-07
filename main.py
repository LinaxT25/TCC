import Connect
import Close
import User
import DataSorting
import DataExport

if __name__ == '__main__':

    print("Input the user ID.")
    userID = input()

    connection = Connect.connect()
    user = User.retrieveActor(connection, userID)
    # userList = User.retrieveActors(connection)

    if user is not False:
        print("User found!\n")
        temporalTuple = DataSorting.sorting(connection, userID)

        DataExport.exportToCsv(temporalTuple, userID)
        DataExport.exportToJson(temporalTuple, userID)

        # for tuples in temporalTuple:
        #     print(tuples)
    else:
        print("User not found!\n")

    # if userList is not False:
    #     print("List of users found!\n")
    #
    #     for user in userList:
    #         temporalTuple = DataSorting.sorting(connection, user[0])
    #
    #         DataExport.exportToCsv(temporalTuple, user[0])
    #         DataExport.exportToJson(temporalTuple, user[0])
    # else:
    #     print("User not found!\n")

    Close.closeConnection(connection)
