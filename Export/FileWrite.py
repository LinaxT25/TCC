import os

min_support = 1  # Get minor support threshold with will be used in FPGrowth


def write_percentage(activity_name, activity_sum, total_sum):
    global min_support
    # Creating a new directory for data to be exported
    dir_path = os.getcwd()
    new_dir = os.path.join(dir_path, "Pattern_Output")  # Joined paths to be compatible with more OS

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # Writing to a file patterns output
    f = open("./Pattern_Output/activities_percentage.txt", "at")
    f.write(activity_name + ": " + str(activity_sum) + "\n")
    f.write("Percentage: " + str(activity_sum / total_sum) + "\n\n")
    min_support = (activity_sum / total_sum) if (activity_sum / total_sum) <= min_support else min_support
    f.close()


def write_total_activities(total_sum):
    # Writing to a file patterns output
    f = open("./Pattern_Output/activities_percentage.txt", "at")
    f.write("Total Activities: " + str(total_sum) + " Minor Support Threshold: " + str(min_support) + "\n")
    f.write("############################### END OF FILE ###############################\n")
    f.close()


def write_freq_item_set(freq_item_set):
    # Creating a new directory for data to be exported
    dir_path = os.getcwd()
    new_dir = os.path.join(dir_path, "Pattern_Output")  # Joined paths to be compatible with more OS

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # Writing to a file patterns output
    f = open("./Pattern_Output/freq_item_output.txt", "wt")
    for frequency in freq_item_set:
        f.write(frequency.__str__() + "\n")
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
