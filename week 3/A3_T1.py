# A3_T1

print("Program starting")
print("Insert two integers.")
num1 = int(input("Insert first integer: "))
num2 = int(input("Insert second integer: "))
print("Comparing inserted integers.")

if num1 == num2:
    print("Integers are the same.")
elif num1 > num2:
    print("First integer is greater.")
else:
    print("Second integer is greater.")

print("Adding integers together.")
sum = num1 + num2
print(f"{num1} + {num2} = {sum}")

print("Checking the parity of the sum...")
if sum % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")

print("Program ending.")
