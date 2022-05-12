#map function

#title case the names
names = ['alfred', 'tabitha', 'william', 'arla']
names_corrected_case = map(lambda x: x.title(), names)
print(list(names_corrected_case))

#other way
names_corrected_case = map(str.title, names)
print(list(names_corrected_case))

#format currency based on country - By Priti
lst = [2.54, 4.0, 3, 9.95, 5.4]
country="India"
if(country == "India"):
    print(list(map("₹ {:,.2f}".format, map(lambda x: x,lst))))
else:
    print(list(map("$ {:,.2f}".format, map(lambda x: x,lst))))

#Using map() function and lambda and count() function create a list which consists of the number of occurence of letter: a.
lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
print(list(map(lambda x: x.count('a') ,lst1)))

#simple use cas to filter items - By Priti
scores =[20,30,40,10,5,4]
print(list(filter(lambda score: score > 20,scores)))

#To get all the countries whose populations are greater than 300 million
countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]
print(list(filter(lambda country: country[1]>300000000,countries)))

aquarium_creatures = [
  {"name": "sammy", "species": "shark", "tank number": "11", "type": "fish"},
  {"name": "ashley", "species": "crab", "tank number": "25", "type": "shellfish"},
  {"name": "jo", "species": "guppy", "tank number": "18", "type": "fish"},
  {"name": "jackie", "species": "lobster", "tank number": "21", "type": "shellfish"},
  {"name": "charlie", "species": "clownfish", "tank number": "12", "type": "fish"},
  {"name": "olly", "species": "green turtle", "tank number": "34", "type": "turtle"}
]
#search all crab species
filter_result = filter(lambda ele : ele['species'] is 'crab' ,map(lambda x: x , aquarium_creatures))
print(list(filter_result))
#filter based on key and value
aquarium_species = filter(lambda ele,search_key='species', search_val='crab': ele[search_key] is search_val ,map(lambda x: x , aquarium_creatures))
aquarium_type = filter(lambda ele,search_key='type', search_val='fish': ele[search_key] is search_val ,map(lambda x: x , aquarium_creatures))


