class PascalCaseClass():
    
    #all methods are functions but not all functions are methods
    
    def method_1(self):
        print("Calling the first method")
        
    def method_2(self): 
        print("Calling the first method")
        
my_instance = PascalCaseClass()
my_other_instance = PascalCaseClass()

my_instance.method_1()

class Player():
    def play (self, name):
        print(f'Ready to play {name}?')
        
player_instance = Player()
player_instance.play('Liam')

#boiler plate code ideally doesn't need to be there but if it does can use __init__

#magic methods are never called directly - define behaviour for some python syntax

#inheritance
#can inherit attributes and methods from base class so child class can do everything base class can do 

class Cylinder():
    def __init__(self, height, radius=1):
        self.height = height
        self.radius = radius
        self.surface_area = self.get_surface_area()
        self.volume = self.get_volume()
        
    def get_surface_area(self):
        self.surface_area = 2 * 3.14 * self.height * self.radius
        return '%.2f' % self.surface_area
        
    def get_volume(self):
        self.volume = 3.14 * (self.radius^2) * self.height
        return '%.2f' % self.volume
        
        
        
my_cylinder = Cylinder(5, 6)

s = my_cylinder.surface_area
v = my_cylinder.volume

print(s, v, " ")


class Car(): 
    def __init__(self, model, year=2022):
        self.model = model
        self.year = year
        self.miles_driven = 0
        
    def drive(self):
        print("vroom")
        self.miles_driven += 1
        
    def info(self):
        print(f"Miles driven: {self.miles_driven}. Model: {self.model}. Year: {self.year}")
        
my_car = Car('Tesla', 2021)

my_car.drive()
my_car.info()
        







