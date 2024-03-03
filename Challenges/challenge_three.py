def solution(N):
    # Check if N is within the valid range
    if not (1 <= N <= 26):
        return "Invalid input"

    # Define the alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Calculate the number of unique letters needed

    # Adding 1 ensures an equal number of occurrences
    unique_letters = (N + 1) // 2

    # Create the string with equal occurrences of unique letters

    result = ""

    for i in range(unique_letters):
        result += alphabet[i] * 2  # Each letter occurs twice

    # If N is odd, add one more letter to make occurrences equal
    if N % 2 == 1:
        result += alphabet[unique_letters]

    return result

print(solution(8))