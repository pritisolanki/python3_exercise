#Exploring any function
#Does any zone have active charging station

zone_chargingstation ={
    "Zone A":False,
    "Zone 2A":False,
    "Zone B":False,
    "Zone C":False,
    "Zone D":False,
    "Zone X":False,
    "Zone U":False,
    "Zone Z":True,
    "Zone Y":False
}
# One way is iterating over iterable with for loop other way is use any()
print(any(zone_chargingstation.values()))

#How any() help in managing multiple conditions - By Priti
employee_eating_preferences = {
    "jon": {'lunch':True,'snack':True,'tea':True},
    "doe": {'lunch':False,'snack':True,'tea':True},
    "koe": {'lunch':False,'snack':False,'tea':False}
}
#with conditionals
for k,x in employee_eating_preferences.items():
    if x['lunch'] is True or x['snack'] is True or x['tea'] is True:
        print(f'Order Meal for {k}') 
    else:
        print(f'{k} opt out for meal') 

#with any()
for k,v in employee_eating_preferences.items():
    if any(v.values()):
        print(f'Order Meal for {k}') 
    else:
        print(f'{k} opt out for meal') 