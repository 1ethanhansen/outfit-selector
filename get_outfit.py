import random
import yaml

with open("dirty.yaml") as dirty_file:
    dirty_clothes = yaml.load(dirty_file, Loader=yaml.SafeLoader)
with open("outfits.yaml") as outfits_file:
    outfits = yaml.load(outfits_file, Loader=yaml.SafeLoader)

dirty_tops = dirty_clothes[0]["tops"]
dirty_bottoms = dirty_clothes[1]["bottoms"]

clean_outfits = []

for outfit in outfits:
    if outfit[0] in dirty_tops or outfit[1] in dirty_bottoms:
        continue
    clean_outfits.append(outfit)

clean_outfits.sort(key=lambda x: x[0])

random_outfit = random.choice(clean_outfits)
print("You should wear the " + random_outfit[0] + " top with the " + random_outfit[1] + " bottom")

outfits.remove(random_outfit)
dirty_clothes[0]["tops"].append(random_outfit[0])
dirty_clothes[1]["bottoms"].append(random_outfit[1])
with open("dirty.yaml", "w") as dirty_file:
    yaml.dump(dirty_clothes, dirty_file)
with open("outfits.yaml", "w") as outfits_file:
    yaml.dump(outfits, outfits_file)