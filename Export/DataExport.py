import csv
import sys
import os
import psycopg2


def export_to_csv(final_tuple, userid):
    # Creating a new directory for data to be exported
    dir_path = os.getcwd()
    new_dir = os.path.join(dir_path, "./Data_Output")  # Joined paths to be compatible with more OS

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    filename = userid + ".csv"
    with open(os.path.join(new_dir, filename), 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL, doublequote=True, )
        try:
            for i in range(len(final_tuple)):
                writer.writerow((i + 1, final_tuple[i][0], final_tuple[i][1]))
        except csv.Error as e:
            sys.exit(e)


def freq_item_export_csv(freq_item_set):
    # Creating a new directory for data to be exported
    dir_path = os.getcwd()
    new_dir = os.path.join(dir_path, "Pattern_Output")  # Joined paths to be compatible with more OS

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    with open(os.path.join(new_dir, "freq_item_set.csv"), 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL, doublequote=True, )
        try:
            for i in range(len(freq_item_set)):
                writer.writerow([i + 1] + list(freq_item_set[i]))
        except csv.Error as e:
            sys.exit(e)


def association_rules_export_csv(association_rules):
    # Creating a new directory for data to be exported
    dir_path = os.getcwd()
    new_dir = os.path.join(dir_path, "Pattern_Output")  # Joined paths to be compatible with more OS

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    with open(os.path.join(new_dir, "association_rules.csv"), 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL, doublequote=True, )
        try:
            for i in range(len(association_rules)):
                writer.writerow([i+1] + association_rules[i])
        except csv.Error as e:
            sys.exit(e)


def export_to_db(final_tuple, userid, connect):
    try:
        cursor = connect.cursor()

        cursor.execute('select exists(select * from information_schema.tables where table_name=%s)',
                       ('standard',))

        if cursor.fetchone()[0] is False:
            create = 'CREATE TABLE "dv8fromtheworld/jda".standard (user_id text,activity text,activity_date date);'
            cursor.execute(create)
            connect.commit()

        filtered_tuple = list(filter(lambda x: x[1] is not None, final_tuple))

        # Remove the 6 values boolean with has been appended in the end of tuple
        for i in range(len(filtered_tuple) - 6):
            insert = 'INSERT INTO "dv8fromtheworld/jda".standard VALUES(%s, %s, %s);'
            cursor.execute(insert, (userid, filtered_tuple[i][0], filtered_tuple[i][1]))

        connect.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
