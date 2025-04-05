def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def check_prime():
    try:
        num = int(input("Enter an integer: "))
        if is_prime(num):
            print(f"The number {num} is a prime number.")
        else:
            print(f"The number {num} is not a prime number.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def list_primes_up_to_limit():
    try:
        limit = int(input("Enter the limit: "))
        print(f"Prime numbers up to {limit}:")
        primes = [num for num in range(2, limit + 1) if is_prime(num)]
        print(primes)
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Main program
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Check if a number is prime")
        print("2. List all prime numbers up to a limit")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            check_prime()
        elif choice == '2':
            list_primes_up_to_limit()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
