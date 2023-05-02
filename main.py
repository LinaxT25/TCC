import Connect
import Close
import User
import DataSorting

if __name__ == '__main__':

    print("Input the user ID.")
    userID = input()

    connection = Connect.connect()
    user = User.retrieveActors(connection, userID)

    if user is not False:
        print("User found!\n")
        temporalTuple = DataSorting.sorting(connection, userID)

    else:
        print("User not found!\n")

    Close.closeConnection(connection)
