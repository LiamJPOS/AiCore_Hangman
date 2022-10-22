#Void Functions return None
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
