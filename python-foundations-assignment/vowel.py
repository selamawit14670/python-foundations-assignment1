# vowels.py

# Function to count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"  # List of vowels
    count = 0  # Initialize counter

    # Loop through each character in the string
    for char in text:
        if char in vowels:
            count += 1  # Increase count if vowel

    return count


# Take input from user
user_input = input("Enter a string: ")

# Print the result
print("Number of vowels:", count_vowels(user_input))