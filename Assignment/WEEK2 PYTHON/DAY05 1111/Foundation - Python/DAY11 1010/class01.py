# OOP - objects - Reusability
# Blueprint - 1; But Multiple Similar Products
# Class - Blueprint - Always starts with Capital Case
    # Attributes - Data - Properties - Variables - Defines the Class
    # Methods/Functions - Actions - Activity - Behaviour of the Class
# Objects - Instances - Encapulates the Attributes & methods of the class
# Access
# Inheritance
# Polymorphism
# Composition
# Abstraction
# Encapsulation
# Method Overriding
# class ClassName:
    # var1 = Val1

    # def method_1(self):
        # statements/expr/returns/pass

# Obj1 = ClassName()


# Class Definition
class Car:
    model = "Altroz" # Attribute

    def display_details(self): # Method
        print("This is Car with model {}".format(self.model)) #Action the method going to perform

my_car = Car() # Object Creation
my_car.display_details() # Accessing of the Class Attributes & Methods


# self - is positional - If I need to access attribute, I need Self at a 1st position. self is not a mandate keyword
# Constructor
# Class Definition
class Car:
    def __init__(self, model, color): # Constructor - Automatically Initializes when creating any object
        self.model = model # Attribute
        self.color = color

    def display_details(self): # Method
        print("This is Car with model {} and its {}".format(self.model, self.color)) #Action the method going to perform

my_car = Car("Altroz", "Red") # Object Creation
my_car.display_details() # Accessing of the Class Attributes & Methods

# Access Specifier - What an Object can access from the Class
# 3 Types
# Public - Objects can access from anywhere within or outside; this is default
# Protected - defined with a _ as a prefix; This can be accessed within class, subclass and object(not recomended)
# Private - defined with a __ as a prefix; This can be accessed only within class
# Class Definition
class Car:
    def __init__(self, model, color): # Constructor - Automatically Initializes when creating any object - Private
        self.model = model # Attribute - Public
        self.color = color # Public Attribute

    def display_details(self): # Method - public
        print("This is Car with model {} and its {}".format(self.model, self.color)) #Action the method going to perform

my_car = Car("Altroz", "Red") # Object Creation
my_car.display_details() # Accessing of the Class Attributes & Methods - Public method
print(my_car.model) # accessing public attribute
print(my_car.color) # accessing public attribute

# Protected
class Car:
    def __init__(self, model, color): # Constructor - Automatically Initializes when creating any object - Private
        self.model = model # Attribute - Public
        self._color = color # Protected Attribute

    def display_details(self): # Method - public
        print("This is Car with model {} and its {}".format(self.model, self._color)) #Action the method going to perform

my_car = Car("Altroz", "Red") # Object Creation
my_car.display_details() # Accessing of the Class Attributes & Methods - Public method
print(my_car.model) # accessing public attribute
print(my_car._color) # accessing protected attribute (not recomended)



# Private
class Car:
    def __init__(self, model, color): # Constructor - Automatically Initializes when creating any object - Private
        self.model = model # Attribute - Public
        self.__color = color # Private Attribute

    def display_details(self): # Method - public
        print("This is Car with model {} and its {}".format(self.model, self.__color)) #Action the method going to perform

my_car = Car("Altroz", "Red") # Object Creation
my_car.display_details() # Accessing of the Class Attributes & Methods - Public method
print(my_car.model) # accessing public attribute
print(my_car.__color) # accessing private attribute (Attribute Error)


# Inheritance - class going to get created from another class - Child class inherit the data and methods from parent class
# Single - 1 Parent
# Multiple - more than 1 parent
# Multilevel - Parent - Child - Sub Child ..
# Hierarchial - 1 Parent - Multi Child - Tree Structure
# Hybrid - Mix of the above

# class ParentClass:
    # pass

# class ChildClass(ParentClass):
    # pass






# single inheritance
class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def start(self):
        print("{} vehicle is started!".format(self.manufacturer))

class Car(Vehicle):
    def __init__(self, manufacturer, model, color):
        super().__init__(manufacturer)
        self.model = model
        self.__color = color

    def display_details(self): # Method - public
        print("This is Car from {} with model {} and its {}".format(self.manufacturer, self.model, self.__color)) #Action the method going to perform

sample_vehicle = Vehicle("Tata") # Object 1 - using class Vehicle
sample_vehicle.start()

my_car = Car("Hundai", "i20", "Red") # Object 2 - using child class Car
my_car.start() # inherited method from parent class
my_car.display_details() # method from child class
# We need to inherit only when we have a child is a relationship with parent



# Multiple
class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def start(self):
        print("{} vehicle is started!".format(self.manufacturer))

class Product():
    def __init__(self, regNum):
        self.regNum = regNum

    def product_details(self):
        print("This car is having an registration number of {}".format(self.regNum))

class Car(Vehicle, Product):
    def __init__(self, manufacturer, regNum, model, color):
        # super().__init__(manufacturer, regNum)
        # super().__init__(regNum)
        Vehicle.__init__(self, manufacturer)
        Product.__init__(self, regNum)
        self.model = model
        self.__color = color

    def display_details(self): # Method - public
        print("This is Car from {} with model {} and its {} with a registration number as {}".format(self.manufacturer, self.model, self.__color, self.regNum)) #Action the method going to perform

sample_vehicle = Vehicle("Tata") # Object 1 - using class Vehicle
sample_vehicle.start()

my_car = Car("Hundai", "AB 45 C 2345", "i20", "Red") # Object 2 - using child class Car
my_car.start() # inherited method from parent class
my_car.product_details()
my_car.display_details() # method from child class





# Multilevel
class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def start(self):
        print("{} vehicle is started!".format(self.manufacturer))

class Car(Vehicle):
    def __init__(self, manufacturer,model, color):
        super().__init__(manufacturer)
        self.model = model
        self.__color = color

    def display_details(self): # Method - public
        print("This is Car from {} with model {} and its {}".format(self.manufacturer, self.model, self.__color)) #Action the method going to perform

class ElectricCar(Car):
    def __init__(self, manufacturer, model, color, batter_capacity):
        super().__init__(manufacturer, model, color)
        self.batter_capacity = batter_capacity
    
    def display_battery_details(self):
        print("This is an Electric car with a capacity of {} kWh".format(self.batter_capacity))

sample_vehicle = Vehicle("Tata") # Object 1 - using class Vehicle
sample_vehicle.start()

my_car = ElectricCar("Hundai", "i20", "Red", 150) # Object 2 - using child class Car
my_car.start() # inherited method from parent class
my_car.display_details() # method from child class
my_car.display_battery_details()



# Hierarchial
class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def start(self):
        print("{} vehicle is started!".format(self.manufacturer))

class Car(Vehicle):
    def __init__(self, manufacturer,model, color):
        super().__init__(manufacturer)
        self.model = model
        self.__color = color

    def display_details(self): # Method - public
        print("This is Car from {} with model {} and its {}".format(self.manufacturer, self.model, self.__color)) #Action the method going to perform

class Bike(Vehicle):
    def __init__(self, manufacturer, bike_type):
        super().__init__(manufacturer)
        self.bike_type = bike_type
    
    def display_bike_details(self):
        print("This is Bike from {} with type {}".format(self.manufacturer, self.bike_type)) #Action the method going to perform


my_car = Car("Hundai", "i20", "Red") # Object 2 - using child class Car
my_car.start() # inherited method from parent class
my_car.display_details() # method from child class

my_bike = Bike("Bajaj", "Avenger 220 Cruise") # Object 2 - using child class Car
my_bike.start() # inherited method from parent class
my_bike.display_bike_details() # method from child class




#######################################################


# Hybrid
class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def start(self):
        print("{} vehicle is started!".format(self.manufacturer))

class Product():
    def __init__(self, regNum):
        self.regNum = regNum

    def product_details(self):
        print("This car is having an registration number of {}".format(self.regNum))

class Car(Vehicle, Product):
    def __init__(self, manufacturer, regNum, model, color):
        Vehicle.__init__(self, manufacturer)
        Product.__init__(self, regNum)
        self.model = model
        self.__color = color

    def display_details(self): # Method - public
        print("This is Car from {} with model {} and its {} with a registration number as {}".format(self.manufacturer, self.model, self.__color, self.regNum)) #Action the method going to perform

class ElectricCar(Car):
    def __init__(self, manufacturer, regNum, model, color, batter_capacity):
        super().__init__(manufacturer, model, regNum, color)
        self.batter_capacity = batter_capacity
    
    def display_battery_details(self):
        print("This is an Electric car with a capacity of {} kWh".format(self.batter_capacity))

class Bike(Vehicle):
    def __init__(self, manufacturer, bike_type):
        super().__init__(manufacturer)
        self.bike_type = bike_type
    
    def display_bike_details(self):
        print("This is Bike from {} with type {}".format(self.manufacturer, self.bike_type)) #Action the method going to perform


my_car = Car("Hundai", "AB 33 C 4567", "i20", "Red") # Object 2 - using child class Car
my_car.start() # inherited method from parent class
my_car.display_details() # method from child class

my_bike = Bike("Bajaj", "Avenger 220 Cruise") # Object 2 - using child class Car
my_bike.start() # inherited method from parent class
my_bike.display_bike_details() # method from child class

my_car1 = ElectricCar("Hundai", "XY 12 Z 9876", "i20", "Red", 150) # Object 2 - using child class Car
my_car1.start() # inherited method from parent class
my_car1.display_details() # method from child class
my_car1.display_battery_details()



#####################################################################################################



# Polymorphism - many forms - same method - based on the object - Over riding
# Method Overriding - Override a method depends on the object or where it is being called

class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def start(self):
        print("{} vehicle is started!".format(self.manufacturer))

class Product():
    def __init__(self, regNum):
        self.regNum = regNum

    def product_details(self):
        print("This car is having an registration number of {}".format(self.regNum))

class Car(Vehicle, Product):
    def __init__(self, manufacturer, regNum, model, color):
        Vehicle.__init__(self, manufacturer)
        Product.__init__(self, regNum)
        self.model = model
        self.__color = color

    def display_details(self): # Method - public
        print("This is Car from {} with model {} and its {} with a registration number as {}".format(self.manufacturer, self.model, self.__color, self.regNum)) #Action the method going to perform

    def start(self):
        print("{} vehicle Roars!".format(self.manufacturer))

class ElectricCar(Car):
    def __init__(self, manufacturer, regNum, model, color, batter_capacity):
        super().__init__(manufacturer, model, regNum, color)
        self.batter_capacity = batter_capacity
    
    def display_battery_details(self):
        print("This is an Electric car with a capacity of {} kWh".format(self.batter_capacity))
    
    def start(self):
        print("{} vehicle is silently starts!".format(self.manufacturer))

class Bike(Vehicle):
    def __init__(self, manufacturer, bike_type):
        super().__init__(manufacturer)
        self.bike_type = bike_type
    
    def display_bike_details(self):
        print("This is Bike from {} with type {}".format(self.manufacturer, self.bike_type)) #Action the method going to perform
    
    def start(self):
        print("{} vehicle vrooms!".format(self.manufacturer))

sample_vehicle = Vehicle("Tata") # Object 1 - using class Vehicle
sample_vehicle.start()

my_car = Car("Hundai", "AB 33 C 4567", "i20", "Red") # Object 2 - using child class Car
my_car.start() # inherited method from parent class
my_car.display_details() # method from child class

my_bike = Bike("Bajaj", "Avenger 220 Cruise") # Object 2 - using child class Car
my_bike.start() # inherited method from parent class
my_bike.display_bike_details() # method from child class

my_car1 = ElectricCar("Hundai", "XY 12 Z 9876", "i20", "Red", 150) # Object 2 - using child class Car
my_car1.start() # inherited method from parent class
my_car1.display_details() # method from child class
my_car1.display_battery_details()



















############################################################################

# Access specifiers/Modifiers for methods

class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def start(self):
        print("{} vehicle is started!".format(self.manufacturer))

    def _protected_method(self):  # Protected method
        print("{} vehicle has a protected method!".format(self.manufacturer))
    
    def __private_method(self):  # Private method
        print("{} vehicle has a private method!".format(self.manufacturer))
    
    def access_private_method(self):  # Public method to access private method
        self.__private_method()

class Product():
    def __init__(self, regNum):
        self.regNum = regNum

    def product_details(self):
        print("This car is having an registration number of {}".format(self.regNum))

class Car(Vehicle, Product):
    def __init__(self, manufacturer, regNum, model, color):
        Vehicle.__init__(self, manufacturer)
        Product.__init__(self, regNum)
        self.model = model
        self.__color = color

    def display_details(self): # Method - public
        print("This is Car from {} with model {} and its {} with a registration number as {}".format(self.manufacturer, self.model, self.__color, self.regNum)) #Action the method going to perform

    def start(self):
        print("{} vehicle Roars!".format(self.manufacturer))
        self._protected_method()  # Accessing protected method
        # self.__private_method() # will throw error
        self.access_private_method()  # Accessing private method

sample_vehicle = Vehicle("Tata") # Object 1 - using class Vehicle
sample_vehicle.start()

my_car = Car("Hundai", "AB 33 C 4567", "i20", "Red") # Object 2 - using child class Car
my_car.start() # inherited method from parent class
my_car.display_details() # method from child class
# my_car.__private_method() # throws error as we cannot access the private methods outside class
my_car._protected_method() # not recommended
my_car.access_private_method()







# Composition - similar to inheritance but needs to have has a relationship

class Engine:
    def __init__(self, hp):
        self.hp = hp
    def start(self):
        print("Engine with {} HP is starting!".format(self.hp))

class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def start(self):
        print("{} vehicle is started!".format(self.manufacturer))

class Car(Vehicle):
    def __init__(self, manufacturer, model, color, hp):
        super().__init__(manufacturer)
        self.model = model
        self.__color = color
        self.engine = Engine(hp)

    def display_details(self): # Method - public
        print("This is Car from {} with model {} and its {}".format(self.manufacturer, self.model, self.__color)) #Action the method going to perform
        self.engine.start()

sample_vehicle = Vehicle("Tata") # Object 1 - using class Vehicle
sample_vehicle.start()

my_car = Car("Hundai", "i20", "Red", 18) # Object 2 - using child class Car
my_car.start() # inherited method from parent class
my_car.display_details() # method from child class