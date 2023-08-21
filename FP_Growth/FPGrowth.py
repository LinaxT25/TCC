import os
import pyfpgrowth

from FP_Growth import ActivitiesExtract
from FP_Growth import Graphs


def fp_growth():
    activity_list = ActivitiesExtract.data_pattern()
    # First analysis
    patterns = pyfpgrowth.find_frequent_patterns(activity_list, 1)
    rules = pyfpgrowth.generate_association_rules(patterns, 0.1)
    Graphs.graphs(patterns, rules)

    # Creating a new directory for data to be exported
    dir_path = os.getcwd()
    new_dir = os.path.join(dir_path, "Pattern_Output")  # Joined paths to be compatible with more OS

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # Writing to a file patterns output
    f = open("./Pattern_Output/pattern1_output.txt", "wt")
    for items in patterns.items():
        f.write(items.__str__() + "\n")
    f.close()

    # Write to a file patterns that are associated with another
    f = open("./Pattern_Output/rules1_output.txt", "wt")
    for items in rules.items():
        f.write(items.__str__() + "\n")
    f.close()

    # Second analysis
    patterns = pyfpgrowth.find_frequent_patterns(activity_list, 2)
    rules = pyfpgrowth.generate_association_rules(patterns, 0.5)

    # Writing to a file patterns output
    f = open("./Pattern_Output/pattern2_output.txt", "wt")
    for items in patterns.items():
        f.write(items.__str__() + "\n")
    f.close()

    # Write to a file patterns that are associated with another
    f = open("./Pattern_Output/rules2_output.txt", "wt")
    for items in rules.items():
        f.write(items.__str__() + "\n")
    f.close()

    # Third analysis
    patterns = pyfpgrowth.find_frequent_patterns(activity_list, 3)
    rules = pyfpgrowth.generate_association_rules(patterns, 0.7)

    # Writing to a file patterns output
    f = open("./Pattern_Output/pattern3_output.txt", "wt")
    for items in patterns.items():
        f.write(items.__str__() + "\n")
    f.close()

    # Write to a file patterns that are associated with another
    f = open("./Pattern_Output/rules3_output.txt", "wt")
    for items in rules.items():
        f.write(items.__str__() + "\n")
    f.close()
