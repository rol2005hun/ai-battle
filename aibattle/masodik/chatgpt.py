def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_checker():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"The number {num} is a prime number.")
    else:
        print(f"The number {num} is not a prime number.")

def list_primes_up_to():
    limit = int(input("Enter the limit: "))
    primes = [n for n in range(2, limit + 1) if is_prime(n)]
    print("Prime numbers up to", limit, ":", primes)

# Running the functions
prime_checker()
list_primes_up_to()