import json
import pprint

# Reading the input file
with open('input_original.ini') as inp:
    data = inp.readlines()

final_list = []
for i in data:
    every_data = i.split('|')
    # Removing '\n' if present in the end.
    if every_data[-1].endswith("\n"):
        every_data[-1] = every_data[-1][:-1]

    # Removing all the data except the ones with a weblink.
    if (every_data[-1].startswith("https://")):
        final_list.append(every_data)

final_dictionary = {}

for path in final_list:
    current_level = final_dictionary
    for i in range(len(path)-2):
        if path[i] not in current_level:
            current_level[path[i]] = {}
        current_level = current_level[path[i]]
    current_level[path[-2]] = path[-1]

print()
pprint.pprint(final_dictionary, depth=10)
print()


with open('op.json', 'w') as op:
    json.dump(final_dictionary, op)
