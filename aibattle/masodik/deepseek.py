def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def list_primes_up_to(limit):
    """List all prime numbers up to a specified limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    # Part 1: Check if a number is prime
    number = int(input("Enter a number to check if it's prime: "))
    if is_prime(number):
        print(f"The number {number} is a prime number.")
    else:
        print(f"The number {number} is not a prime number.")

    # Part 2: List all prime numbers up to a specified limit
    limit = int(input("Enter a limit to find all prime numbers up to that limit: "))
    primes = list_primes_up_to(limit)
    print(f"Prime numbers up to {limit}: {primes}")

if __name__ == "__main__":
    main()