"""
 * @author Aarav Chandra
 * @create date 2020-07-22 00:28:11
 * @modify date 2020-07-22 00:28:11
 """

import json
import pprint

# Reading the input file
with open('input_original.ini') as inp:
    data = inp.readlines()

final_dictionary = {}
final_list = []

# FIltering the required info. and storing in a list of list.
for i in data:
    every_data = i.split('|')
    # Removing '\n' if present in the end.
    if every_data[-1].endswith("\n"):
        every_data[-1] = every_data[-1][:-1]

    # Removing all the data except the ones with a weblink.
    if (every_data[-1].startswith("https://")):
        final_list.append(every_data)

# Converting to nested dictionary
for path in final_list:
    current_level = final_dictionary
    # loop for individual keys added in nested dict until 3rd last element.
    for i in range(len(path)-2):
        if path[i] not in current_level:
            current_level[path[i]] = {}
        current_level = current_level[path[i]]
    # making last element as the value of the previous element
    current_level[path[-2]] = path[-1]

print()
pprint.pprint(final_dictionary, depth=10)
print()

# Writing the output in JSON format to a format.
with open('op.json', 'w') as op:
    json.dump(final_dictionary, op)
