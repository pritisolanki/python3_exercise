#Dictionary Exercise - Practiced by Priti
#convert two list in to dictionary
list1 = range(1,6)
list2 = ['pink','red','yellow','orange','blue']

print(zip(list1,list2)) #return <zip object at 0x1060a71c0>
print(dict(zip(list1,list2)))

# Initialize dictionary with default values
employee={"Simi","Sally"}
default_employee_assignments= {"Team":'Engineering',"In Time":"9:00 AM", "Lunch Time":"Oops!"}
employee_onboarding = dict.fromkeys(employee,default_employee_assignments)
print(employee_onboarding)

#check is value is there or not
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in a dict')

print(f'Find minimum: min(sample_dict)')

# check if key exists
#Removed. dict.has_key() – use the in operator instead.
if 'a' in sample_dict.keys(): 
    print('key exists')

#dictionary view operators
fruit_dict = {'apple':'green','banana':'yellow','orange':'orange'}
unkown_fruit_dict = {'bel':'green','ber':'yellow','orange':'black','mystic':'yellow'}

dict_1 = fruit_dict.keys()  & unkown_fruit_dict.keys()
print(f'intersection: {dict_1}')

dict_2 = fruit_dict.keys()  ^ unkown_fruit_dict.keys()
print(f'symmetric diff: {dict_2}')

dict_3 = fruit_dict.keys()  - unkown_fruit_dict.keys()
print(f'difference: {dict_3}')

dict_4 = fruit_dict.keys()  | unkown_fruit_dict.keys()
print(f'union {dict_4}')


print(f'remove fruit: { unkown_fruit_dict.pop("ber") }')

#Find all yellow flowers : Using dictionary comprehension
flower_dict = {'rose':'red','sunflower':'yellow','marigold':'yellow','jasmine':'white','lily':'pink'}
yellow_flower= { x for x in flower_dict.items() if "yellow" in x }
print(dict(yellow_flower))