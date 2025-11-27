# my own work

print("Program starting.")
print("Estimate how many minutes you spent on programming...")
m1 = int(input("A1_T1: "))
m2 = int(input("A1_T2: "))
m3 = int(input("A1_T3: "))
m4 = int(input("A1_T4: "))
m5 = int(input("A1_T5: "))
m6 = int(input("A1_T6: "))
m7 = int(input("A1_T7: "))
Sum = m1 + m2 + m3 + m4 + m5 + m6 + m7
print(f"In total you spent {Sum} minutes on programming.")
average = Sum / 7
average_rounded = round(average)
print(
    f"Average per task was {average} min and same rounded to the nearest integer {average_rounded} min. ")
print("program ending")
