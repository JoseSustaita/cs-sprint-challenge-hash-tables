def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    result = []

    # Loop through nums
    for nums in a:

        #If in cache
        if cache.get(abs(nums)):
            if (cache.get(abs(nums)) + nums) == 0:
                result.append(abs(nums))
        else:
            cache[abs(nums)] = nums

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
