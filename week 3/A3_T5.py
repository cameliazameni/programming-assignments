print("program starting...\n")

print("Options:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("Exit")
choice = input("Choose an option (1/2/3): ")

if choice == 1:
            c = float(input("Enter temperature in Celsius: "))
            f = celsius_to_fahrenheit(c)
            print(f"{round(f, 1)} °F\n")

        elif choice == 2:
            f = float(input("Enter temperature in Fahrenheit: "))
            c = fahrenheit_to_celsius(f)
            print(f"{round(c, 1)} °C\n")

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.\n")

            if __name__ == "__main__":
                main()
