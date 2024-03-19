def fibonacci(n):
 """
 Generates the Fibonacci sequence up to a specified term n using iteration.

 Args:
   n: The number of terms in the Fibonacci sequence.

 Returns:
   A list containing the Fibonacci sequence up to n terms.
 """

 if n <= 1:
   return [n]  # Base case: Return a list with the first term (0 or 1)
 else:
   a, b = 0, 1  # Initialize the first two terms
   fib_sequence = [a, b]  # Create a list to store the sequence
   for _ in range(2, n + 1):
     c = a + b  # Calculate the next term
     fib_sequence.append(c)  # Add the next term to the list
     a, b = b, c  # Update a and b for the next iteration
   return fib_sequence  # Return the complete Fibonacci sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print("Fibonacci sequence:", fibonacci_sequence)
