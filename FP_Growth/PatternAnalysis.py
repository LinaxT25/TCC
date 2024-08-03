import psycopg2

from DB import Connect
from FP_Growth.fpgrowth_algorithm.fpgrowth import fpgrowth


def db_extract_data():
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


def fp_growth():
    activity_list = db_extract_data()

    # For 50% of total actors(4263) and total of activities in list(4109): 2131,5 / 4109
    # freq_item_set, association_rules = fpgrowth(activity_list, min_sup_ratio=0.5187, min_conf=0.1)

    # For 25% of total actors(4263) and total of activities in list(4109): 1065,75 / 4109
    freq_item_set, association_rules = fpgrowth(activity_list, min_sup_ratio=0.2593, min_conf=0.1)

    # For 10% of total actors(4263) and total of activities in list(4109): 426,3 / 4109
    # freq_item_set, association_rules = fpgrowth(activity_list, min_sup_ratio=0.1037, min_conf=0.1)

    # For 5% of total actors(4263) and total of activities in list(4109): 205,45 / 4109
    # freq_item_set, association_rules = fpgrowth(activity_list, min_sup_ratio=0.05, min_conf=0.1)

    # For 2% of total actors(4263) and total of activities in list(4109): 85,26 / 4109
    # freq_item_set, association_rules = fpgrowth(activity_list, min_sup_ratio=0.0207, min_conf=0.1)

    # For 1% of total actors(4263) and total of activities in list(4109): 42,63 / 4109
    # freq_item_set, association_rules = fpgrowth(activity_list, min_sup_ratio=0.0103, min_conf=0.1)
