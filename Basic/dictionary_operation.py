# Find all yellow flowers : Using dictionary comprehension - by Priti
flower_dict = {
    "rose": "red",
    "sunflower": "yellow",
    "marigold": "yellow",
    "jasmine": "white",
    "lily": "pink",
}
yellow_flower = {x for x in flower_dict.items() if "yellow" in x}
print(yellow_flower)
