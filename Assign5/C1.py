from collections import defaultdict

keys = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII', 'Class-VIII']
values = [1, 2, 2, 3, 2]

# Create a defaultdict with set as the default factory
result_dict = defaultdict(set)

# Populate the dictionary using the lists
for key, value in zip(keys, values):
    result_dict[key].add(value)

# Convert the defaultdict to a regular dictionary
final_dict = dict(result_dict)

print(result_dict)