def digit_sum(num):
    # function to calculate the sum of digits for a given number
    return sum(int(digit) for digit in str(num))


def max_sum_with_equal_digit_sum(A):
    max_sum = -1
    # Iterate through all pairs of numbers
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            # Calculate the sum of digits for each number in the pair
            sum_i = digit_sum(A[i])
            sum_j = digit_sum(A[j])
            # If the sums of digits are equal for the pair
            if sum_i == sum_j:
                # Update the maximum sum if the sum of the pair is greater
                max_sum = max(max_sum, A[i] + A[j])
    # Return the maximum sum found or -1 if no such pair was found
    return max_sum if max_sum >= 0 else -1


# Example usage:
A = [51, 32, 43]
print( max_sum_with_equal_digit_sum(A))
