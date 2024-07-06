#1 
# def greet():
#     print("Hello, world!")

# greet()  # Direct call


#2 
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")  # Call with an argument

#3 
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet(name="Alice", message="Good morning")  # Call with keyword arguments
greet("Alice")  # Call with default keyword argument
