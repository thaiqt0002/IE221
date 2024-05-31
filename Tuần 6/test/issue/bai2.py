# Define a function 'is_sorted_ascending' to check if a list is sorted in ascending order.
def is_sorted_ascending(lst):
    # Check if all elements at index i are less than or equal to elements at index i+1.
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))