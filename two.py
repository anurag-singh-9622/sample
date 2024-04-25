# Sample Python code with functions, classes, and variables

# Define a function to calculate the square of a number
def calculate_square(num):
    return num ** 2

# Define a class for a person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Define some variables
number = 5
name = "John"
age = 25

# Call the calculate_square function
result = calculate_square(number)
print(f"The square of {number} is {result}")

# Create an instance of the Person class and call the greet method
person = Person(name, age)
person.greet()
