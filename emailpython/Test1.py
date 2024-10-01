def min_operations_to_permutation(arr):
    n = len(arr)
    # Step 1: Count frequency of each number in the array
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 2: Initialize the operations counter
    operations = 0

    # Step 3: Iterate through each number from 1 to N
    for i in range(1, n + 1):
        if i in freq and freq[i] > 0:
            freq[i] -= 1  # If i is present, decrease its frequency
        else:
            # If i is missing, find the next highest frequency number to adjust
            while True:
                # Find a number that has extra occurrences
                for j in range(1, n + 1):
                    if j in freq and freq[j] > 1:
                        # Replace one occurrence of j with i
                        operations += abs(j - i)
                        freq[j] -= 1
                        break
                else:
                    continue
                break

    return operations


# Example usage
arr = [3, 2, 1, 4]
result = min_operations_to_permutation(arr)
print(f"Minimum operations required: {result}")
