def generate_fibonacci_sequence(n):
    sequence = [0, 1]  # Initial values of Fibonacci sequence

    if n <= 0:
        return []

    if n == 1:
        return [0]

    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

# Example usage
n = int(input("Enter the number : "))
fibonacci_sequence = generate_fibonacci_sequence(n)

print(f"The Fibonacci sequence up to {n} terms is:")
for number in fibonacci_sequence:
    print(number, end=" ")
