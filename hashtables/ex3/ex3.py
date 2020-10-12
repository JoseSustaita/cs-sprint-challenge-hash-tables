def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
# Your code here

    cache = {}
    result = []

    # Loop through arrays

    for i in arrays:
        for k in i:

            # If element in cache add one else = one
            if k in cache:
                cache[k] += 1
            else:
                cache[k] = 1

# Check to see if it appears in all arrays
    for num in cache:
        if cache[num] == len(arrays):
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
