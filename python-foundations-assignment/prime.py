# prime.py

# Function to check if a number is prime
def is_prime(num):
    # Numbers less than or equal to 1 are not prime
    if num <= 1:
        return False

    # Check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            return False  # Not prime if divisible

    return True  # Prime if no divisors found


# Take input from user
number = int(input("Enter a number: "))

# Check and print result
if is_prime(number):
    print("The number is prime.")
else:
    print("The number is not a prime.")