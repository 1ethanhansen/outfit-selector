import yaml

outfits = []
tops = []
bottoms = []

while True:
    top = input("Enter a top identifier or # to exit: ")
    if top is "#":
        break
    tops.append(top)

while True:
    bottom = input("Enter a bottom identifier or # to exit: ")
    if bottom is "#":
        break
    bottoms.append(bottom)

for top in tops:
    for bottom in bottoms:
        outfits.append([top, bottom])

with open("outfits.yaml", "w") as outfits_file:
    yaml.dump(outfits, outfits_file)
with open("dirty.yaml", "w") as dirty_file:
    empty = [{'tops': []}, {'bottoms': []}]
    yaml.dump(empty, dirty_file)
