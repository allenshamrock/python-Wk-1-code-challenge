def solution(array_a):
    # Get the length of the input array
    length_of_arr = len(array_a)
    # Calculate the total sum of bricks in all boxes
    total_sum = sum(array_a)
    # Calculate the target number of bricks per box
    target = int(total_sum/length_of_arr)

    # Check if the total sum is evenly divisible by the number of boxes
    # and if the target number of bricks per box is not 10
    if total_sum % length_of_arr != 0 or target != 10:
        return (f"{-1} - It is not possible to end up with exactly 10 bricks in each box")

# Initialize variable to store the total number of moves required
    moves_required = 0

    # Iterate through the array, excluding the last element
    for i in range(length_of_arr-1):

        # Calculate the difference between the number of bricks in the current box
        diff = array_a[i] - target
        if diff > 0:
            moves_required += diff
            array_a[i] -= diff
            array_a[i+1] += diff

        elif diff < 0:
            moves_required += abs(diff)
            array_a[i+1] -= abs(diff)
            array_a[i] += abs(diff)

    return f"Minimum number of moves needed:{moves_required}"


print(solution([11, 10, 8, 12, 8, 10, 11]))
