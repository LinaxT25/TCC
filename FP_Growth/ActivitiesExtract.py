import psycopg2

from DB import Connect


def data_pattern():
    try:
        connection = Connect.connect()
        cursor = connection.cursor()

        # Get all users from database for extract the activities
        query = 'SELECT distinct user_id from "dv8fromtheworld/jda".standard'
        cursor.execute(query)
        users = cursor.fetchall()

        # Get all activities from a user and make a list
        activity_list = []  # Global list to store all activities made by users
        for userid in users:
            query = 'SELECT activity from "dv8fromtheworld/jda".standard WHERE "user_id" = %s;'
            cursor.execute(query, (userid,))
            activity = cursor.fetchall()

            user_activity = []  # Local list to store only one user activities
            for i in range(len(activity)):
                # Check for duplicates to not overflow the algorithm
                if not user_activity.__contains__(activity[i][0]):
                    user_activity.append(activity[i][0])
            activity_list.append(user_activity)  # Append to global list

        return activity_list
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
