# Define a function that takes two arguments and returns their sum
def add_numbers(num1, num2):
    return num1 + num2

# Define a class called Person with attributes name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Define some variables
name = "Alice"
age = 25
nums = [1, 2, 3, 4, 5]

# Call the add_numbers function and print the result
result = add_numbers(10, 20)
print(f"Result of adding 10 and 20 is: {result}")

# Create an instance of the Person class and call the introduce method
person = Person(name, age)
person.introduce()

# Print the elements of the nums list
for num in nums:
    print(num)
