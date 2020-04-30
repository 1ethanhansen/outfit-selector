import yaml

with open("dirty.yaml", "w") as dirty_file:
    empty = [{'tops': []}, {'bottoms': []}]
    yaml.dump(empty, dirty_file)
    print("Laundry cleaned!")
