import os


def write_percentage(activity_name, activity_sum, list_length):
    # Creating a new directory for data to be exported
    dir_path = os.getcwd()
    new_dir = os.path.join(dir_path, "Pattern_Output")  # Joined paths to be compatible with more OS

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # Writing to a file patterns output
    f = open("./Pattern_Output/activities_percentage.txt", "at")
    f.write(activity_name + ": " + str(activity_sum) + "\n")
    f.write("Percentage: " + str(activity_sum / list_length) + "\n\n")
    f.close()


def write_freq_item_set(item_set, item_set_sup):
    # Creating a new directory for data to be exported
    dir_path = os.getcwd()
    new_dir = os.path.join(dir_path, "Pattern_Output")  # Joined paths to be compatible with more OS

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # Writing to a file patterns output
    # TODO Check if file already exists
    f = open("./Pattern_Output/freq_item_output.txt", "at")
    f.write(item_set.__str__() + " " + item_set_sup.__str__() + "\n")
    f.close()


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
