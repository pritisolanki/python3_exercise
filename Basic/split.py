# split string

input_string = "lorem,porem,something"
string_list = input_string.split(",")
print(string_list)

# how many splits ?
input_string2 = "lorem,porem,something,exciting,continued"
string2_list = input_string2.split(",", maxsplit=2)
print(string2_list)
