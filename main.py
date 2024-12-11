# Define the test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'coding': 1}

# Print the dictionary
print("Test Dictionary:", test_dict)

# Ask the user to enter a value to check the frequency
value_to_check = int(input("Enter the value you want to check the frequency of: "))

# Calculate and print the frequency of the value
frequency = list(test_dict.values()).count(value_to_check)
print(f"The frequency of the value {value_to_check} in the test dictionary is: {frequency}")
