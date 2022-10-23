#Void Functions return None
from email.policy import default
from sre_compile import isstring

from attr import attributes


def void_function():
    print("This is a void function")

void_result = void_function()
print(void_result)


#Range Checker
def in_range(lower_bound, upper_bound, number):
    if number > lower_bound and number < upper_bound:
        print(f"{number} is between {lower_bound} and {upper_bound}")
    else:
        print(f"{number} is NOT between {lower_bound} and {upper_bound}")
        
in_range(1, 10, 11)

#Volume of a Sphere
def volume_of_sphere(radius):
    pi = 3.14
    answer = 4.0/3.0 * pi * radius**3
    
    return round(answer, 2)
    
print(volume_of_sphere(5))

#%%
#if list is passed in for specific keys, print those keys, otherwise print all

#Default Arguments
def print_attributes(item_of_clothing , attributes_to_print = 'all'):
    attributes = []
    
    if isinstance(attributes_to_print, str):
    
        if attributes_to_print == 'all':
            for i in item_of_clothing:
                attributes.append(i)
        
        if attributes_to_print != 'all':
            split_attributes = attributes_to_print.split(",")
            attributes = [i.strip() for i in split_attributes]
        
    if isinstance(attributes_to_print, list):
        attributes = attributes_to_print
        
    result = ''       
    spacer = ''         
    for attribute in attributes:
        try:
            result = result + spacer + str(item_of_clothing[attribute])
        except KeyError:
           result = result + spacer + 'attribute ' + str(attribute) + "is not found" 
        
        spacer = ', '
                
    print(result)
       
cardigan = {
    "brand": "Topman", 
    "material": "wool",
    "colour" : "grey"
    }
'''
Test Cases for default arguments

#print_attributes({'one':1, 'two':2, 'three':3})
# '1, 2, 3'

#print_attributes({'one':1, 'two':2, 'three':3}, 'all')
# '1, 2, 3'

#print_attributes({'one':1, 'two':2, 'three':3}, ['one', 'three'])
# '1, 3'

#print_attributes({'one':1, 'two':2, 'three':3}, 'one, three')
# '1, 3'

#print_attributes({'one':1, 'two':2, 'three':3}, 'one,three')
# '1, 3'

print_attributes({'one':1, 'two':2, 'three':3}, ['one', 'four', 'three'])
# '1'

#print_attributes({}, ['one'])
# ''
'''