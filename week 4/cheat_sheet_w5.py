#Functions in programming
#what is a function
#Example function in Python

print("")
print("")
#if statement
#For/while loop
#Function

print("Hello")
# Print is an example of a function
# Hello in this case is an example of a parameter


def greet(name):
    return f"Hello, {name}" #return something from a function

message = greet("Mira")
print(message)

# message = greet("Heikki")
# print(message)

# def greeting(): #defining a function
#   print("How do you do") #function content

#   greeting() # Call the function< function call
#   greeting()
#   greeting()

def greeting_airport(person, age):
    print(f"Person: {person}, age: {age}")

    greeting_airport(age=48, person="Mira")