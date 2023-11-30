import csv
import sys
import os
import psycopg2

elements_to_write = 0  # Used to store the index of elements to write


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


def write_association_rules(association_rules):
    # Creating a new directory for data to be exported
    dir_path = os.getcwd()
    new_dir = os.path.join(dir_path, "Pattern_Output")  # Joined paths to be compatible with more OS

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # Write to a file patterns that are associated with another
    f = open("./Pattern_Output/association_rules_output.txt", "wt")
    for rules in association_rules:
        f.write(rules.__str__() + "\n")
    f.close()


def freq_item_export_csv(item_set, item_set_sup, elements, item_set_list):
    global elements_to_write
    # Creating a new directory for data to be exported
    dir_path = os.getcwd()
    new_dir = os.path.join(dir_path, "Pattern_Output")  # Joined paths to be compatible with more OS

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # Check if file exists to choice write a new file or append to an existent file
    if elements_to_write == 0:
        with open(os.path.join(new_dir, "freq_item_set.csv"), 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE, escapechar=' ', quotechar=' ')
            try:
                # Converting the set to a list, for changing in csv format
                item_set = list(item_set)

                # Index
                item_set.insert(0, elements_to_write + 1)
                elements_to_write += 1

                # Manually adding double quotes, writer method causes much error.
                item_set[1] = '"' + item_set[1]
                item_set[-1] = item_set[-1] + '"'

                # Appending the support threshold
                item_set.append(item_set_sup)
                # Appending the ratio support threshold
                item_set.append(item_set_sup / len(item_set_list))

                # Manually adding double quotes for the appends.
                item_set[len(item_set) - 2] = '"' + str(item_set[len(item_set) - 2]) + '"'
                item_set[-1] = '"' + str(item_set[-1]) + '"'

                writer.writerow(item_set)
            except csv.Error as e:
                sys.exit(e)
    else:
        with open(os.path.join(new_dir, "freq_item_set.csv"), 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE, escapechar=' ', quotechar=' ')
            try:
                # Converting the set to a list, for changing in csv format
                item_set = list(item_set)

                # Index
                item_set.insert(0, elements_to_write + 1)
                elements_to_write += 1

                # Manually adding double quotes, writer method causes much error.
                item_set[1] = '"' + item_set[1]
                item_set[-1] = item_set[-1] + '"'

                # Appending the support threshold
                item_set.append(item_set_sup)
                # Appending the ratio support threshold
                item_set.append(item_set_sup / len(item_set_list))

                # Manually adding double quotes for the appends.
                item_set[len(item_set) - 2] = '"' + str(item_set[len(item_set) - 2]) + '"'
                item_set[-1] = '"' + str(item_set[-1]) + '"'

                writer.writerow(item_set)
            except csv.Error as e:
                sys.exit(e)

    # Reset when all elements have passed
    if elements_to_write == elements:
        elements_to_write = 0
