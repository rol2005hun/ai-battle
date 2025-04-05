def is_prime(n):
    """
    Checks if a given number is prime.

    Args:
      n: The number to check.

    Returns:
      True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(num):
    print(f"The number {num} is a prime number.")
else:
    print(f"The number {num} is not a prime number.")

# Find and print all prime numbers up to a limit
limit = int(input("Enter a limit to find prime numbers up to: "))
print("Prime numbers up to", limit, ":")
for num in range(2, limit + 1):
    if is_prime(num):
        print(num, end=" ")