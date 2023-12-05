def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    Args
    values:
    1D array of values (list or numpy array)
    num_iteration:
    Integer to set the number of iterations
    """
    for x in range(num_iterations):
        highest_value = max(values)
        highest_idx = values.index(highest_value)
        
        # Share with left neighbor
        left_neighbor = (highest_idx - 1) % len(values)
        values[left_neighbor] += int(highest_value * share)

        # Share with right neighbor
        right_neighbor = (highest_idx + 1) % len(values)
        values[right_neighbor] += int(highest_value * share)

        # Deduct shared value from the current maximum; two times, because we share it with the right and left neighbor at once
        values[highest_idx] -= 2 * int(highest_value * share) 

        values_new = values

    return values_new
