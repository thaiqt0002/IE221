# Calculate how many egg boxes will be required for a given quantity of eggs.
def boxes_required(egg_qty, box_capacity, box_qty):
    # param qty: Number of eggs.
    # param box_capacity: How many eggs will fit in a box.
    # return: The number of boxes that are required.
    return (int(egg_qty / box_capacity) + 1 == box_qty)