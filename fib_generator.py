def generate_fibonacci(num_terms):
    """
    Generate and print the Fibonacci sequence up to the given number of terms.
    :param num_terms: Number of terms for the Fibonacci sequence (integer)
    """
    # Check if the input is valid
    if num_terms <= 0:
        print("Please enter a positive integer.")
        return

    # If only one term is requested, output 0
    if num_terms == 1:
        print("Fibonacci sequence up to 1 term:")
        print(0)
        return

    # Initialize the first two terms of the Fibonacci sequence
    fib_sequence = [0, 1]

    # Generate the remaining terms of the sequence
    for _ in range(2, num_terms):
        # The next term is the sum of the last two terms
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    # Display the Fibonacci sequence
    print(f"Fibonacci sequence up to {num_terms} terms:")
    print(fib_sequence)

# Take input from the user
try:
    terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
    generate_fibonacci(terms)
except ValueError:
    print("Invalid input! Please enter an integer.")
