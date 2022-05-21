# The all() function is used to check every member of a collection as being truthy or not
# using any and all and understanding short circuit evaluation in python - By Priti
choices = {
    'Jon':{'beans':True,'egg':False,'spiance':True},
    'Sally':{'chicken':False,'egg':False},
    'Molly':{'beans':True,'tamato':True,'spinach':True}
}

for key,options in choices.items():
    if(all(options.values())):
        print(f'{key} enjoys vegetarian food')
    elif(any(options.values())):
        print(f'{key} enjoys both type of food')
    else:
        print(f'{key} enjoy non-veg food')

menu_option = {
    'veg' : ['beans','tamato','spianch','okra','potatoes','onion','olives'],
    'non-veg':['chicken','egg','chicken stock']
}
