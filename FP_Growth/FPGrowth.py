import os
import pyfpgrowth

from FP_Growth import ActivitiesExtract
from fpgrowth_py import fpgrowth
from FP_Growth import Graphs


def fp_growth():
    activity_list = ActivitiesExtract.data_pattern()

    # First analysis
    # MinSupRatio = Number of times an item appears in the database / Number of itemset in the database
    # MinSupRatio for display all activities = 0.0001 or 0,01%
    # freq_item_set, rules = fpgrowth(activity_list, minSupRatio=0.0001, minConf=0.5)
    # patterns = pyfpgrowth.find_frequent_patterns(activity_list, 2)
    # rules = pyfpgrowth.generate_association_rules(patterns, 0.75)

    # Graphs.graph_pattern(patterns, 2)
    # Graphs.graph_rule(rules)

    # # Creating a new directory for data to be exported
    # dir_path = os.getcwd()
    # new_dir = os.path.join(dir_path, "Pattern_Output")  # Joined paths to be compatible with more OS
    #
    # if not os.path.exists(new_dir):
    #     os.makedirs(new_dir)
    #
    # # Writing to a file patterns output
    # f = open("./Pattern_Output/pattern1_output.txt", "wt")
    # for items in freq_item_set:
    #     f.write(items.__str__() + "\n")
    # f.close()
    #
    # # Write to a file patterns that are associated with another
    # f = open("./Pattern_Output/rules1_output.txt", "wt")
    # for items in rules:
    #     f.write(items.__str__() + "\n")
    # f.close()
