from asyncore import read
import readline

import json
#return file as list
file_handle = open("dogs.txt")
dogs_list = file_handle.readlines()

#read file line by line

with open("dogs.txt") as reader:
    for line in reader:
        print(line,end='')

with open("dog_breed_reversed","w") as writer:
    for breed in reversed(dogs_list):
        writer.write(breed)

#read json file
print(json.load(open('sample.json')))