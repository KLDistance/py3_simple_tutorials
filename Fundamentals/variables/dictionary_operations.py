my_dict = {'Wilson' : 'Programmer', 'Jack' : 'Businessman', 'Alice' : 'Doctor'}

print(my_dict['Wilson'])
my_dict['Jack'] = 'Researcher'
print(my_dict['Jack'])

# same key cannot emerge above 1 time, otherwise the latter value is recorded
my_dict2 = {'Wilson' : 'Programmer', 'Wilson' : 'Researcher'}
print(my_dict2)

# clear the dictionary
my_dict.clear()
print(my_dict)

# other details see https://www.runoob.com/python3/python3-dictionary.html
