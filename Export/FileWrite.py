import os

elements_to_write = 0


def write_freq_item_set(item_set, item_set_sup, elements, item_set_list):
    global elements_to_write
    # Creating a new directory for data to be exported
    dir_path = os.getcwd()
    new_dir = os.path.join(dir_path, "Pattern_Output")  # Joined paths to be compatible with more OS

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # Writing to a file patterns output
    if elements_to_write == 0:
        f = open("./Pattern_Output/freq_item_output.txt", "wt")
        f.write(item_set.__str__() + " " + item_set_sup.__str__() + " " + str(item_set_sup / len(item_set_list)) + "\n")
        f.close()
        elements_to_write = 1
    else:
        f = open("./Pattern_Output/freq_item_output.txt", "at")
        f.write(item_set.__str__() + " " + item_set_sup.__str__() + " " + str(item_set_sup/len(item_set_list)) + "\n")
        f.close()
        elements_to_write += 1

    if elements_to_write == elements:
        elements_to_write = 0


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
