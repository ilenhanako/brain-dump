def is_item_in_array(item, array):
    # This function checks if the item is in the array (non-recursive part).
    # Assuming it's a simple presence check for this example.
    return item in array

def open_subarray(subarray):
    # This function 'opens' a subarray. For the sake of this example,
    # let's assume it just returns the subarray itself.
    return subarray

def find_item_in_nested_array(array, item):
    for element in array:
        if isinstance(element, list):  # Check if it's a subarray
            # If it's a subarray, recursively search within it
            if find_item_in_nested_array(open_subarray(element), item):
                return True
        else:
            # If it's not a subarray, check if the item is in this element
            if is_item_in_array(item, element):
                return True
    return False
nested_array = [1, 2, [3, 4], [[5, 6], 7]]
item_to_find = 5

result = find_item_in_nested_array(nested_array, item_to_find)
print(f"Item {item_to_find} found: {result}")