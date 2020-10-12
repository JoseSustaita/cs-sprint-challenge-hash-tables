def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}


# Loop through list of weights
    for item in range(length):
        # if limit - weights is in cache
        if limit - weights[item] in cache:
            # return item
            return [item, cache[limit - weights[item]]]
            # Else add to cache
        else:
            cache[weights[item]] = item

    return None
