# Setup the conversion factor
km_to_miles_factor = 0.621371

# First distance conversion
km_input1 = float(input("Enter distance in kilometers: "))
miles_result1 = km_input1 * km_to_miles_factor
print("Distance in miles:", miles_result1)

# Ask the user if they want to do it again
ask_user = input("Do you want to convert another distance? (yes/no): ")

if ask_user == "yes":
    # Second distance conversion if they typed yes
    km_input2 = float(input("Enter distance in kilometers: "))
    miles_result2 = km_input2 * km_to_miles_factor
    print("Distance in miles:", miles_result2)
else:
    # Say goodbye if they type anything else
    print("Program ended.")