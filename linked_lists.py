# Just my small exercises in linked lists
# Iterate over linked lists
# Class describes one cell (item) of linked lists


class Cell:
    def __init__(self, value=None, next_cell=None):
        self.value = value
        self.next_cell = next_cell

# Linked list creation
e = Cell(10, None)
c = Cell(4, e)
b = Cell(5, c)
a = Cell(10, b)


def iterate_linked_list(head):
    while head:
        print(head.value)
        head = head.next_cell


# Find cell
def find_cell(head, value):
    while head:
        if head.value == value:
            return head
        head = head.next_cell
    return


# Add cell at beginning
def add_new_cell_at_beginning(top, new_cell):
    new_cell.next_cell = top.next_cell
    top.next_cell = new_cell


# Insert cell after given list
def insert_cell_after(after_me: Cell, new_cell: Cell):
    new_cell.next_cell = after_me.next_cell
    after_me.next_cell = new_cell


# Delete cell
def delete_after_cell(after_me: Cell):
    target_cell = after_me.next_cell
    after_me.next_cell = after_me.next_cell.next_cell
    del target_cell


# Insert cell in sorted list
def insert_cell_in_sorted_list(top, new_cell):
    while top.next_cell.value < new_cell.value:

        top = top.next_cell

    new_cell.next_cell = top.next_cell
    top.next_cell = new_cell


# Copying list
def copy_list(old_limiter: Cell):
    new_top = Cell()
    last_added = new_top

    # Pass limiter
    old_cell = old_limiter.next_cell

    # Copying elements
    while old_cell:
        # Creating new elem
        last_added.next_cell = Cell()

        # Go to new elem
        last_added = last_added.next_cell

        # Setup value for new elem
        last_added.value = old_cell.value

        # Preparing to copy new cell
        old_cell = old_cell.next_cell

    last_added.next_cell = None
    return new_top


def insertion_sort(input_cell: Cell):

    # Limiter for output list
    limiter = Cell()
    limiter.next_cell = None
    input_cell = input_cell.next_cell

    while input_cell:
        # Get next cell for adding to list
        next_cell = input_cell

        # Change input_cell to next_cell for next iteration
        input_cell = input_cell.next_cell

        # Finding where elem should be added to output list
        after_me = limiter
        while after_me.next_cell and after_me.next_cell.value < next_cell.value:
            after_me = after_me.next_cell

        # Insert elem in output list
        next_cell.next_cell = after_me.next_cell
        after_me.next_cell = next_cell
    return limiter


def selection_sort(input_cell: Cell):
    limiter = Cell()
    limiter.next_cell = None
    while input_cell.next_cell:
        # Finding item with best value
        best_after_me = input_cell
        best_value = best_after_me.next_cell.value

        # Starting to search next elem
        after_me = input_cell.next_cell
        while after_me.next_cell:
            if after_me.next_cell.value > best_value:
                best_after_me = after_me
                best_value = after_me.next_cell.value
            after_me = after_me.next_cell

        # Deleting needed cell from input list
        best_cell = best_after_me.next_cell
        best_after_me.next_cell = best_cell.next_cell

        best_cell.next_cell = limiter.next_cell
        limiter.next_cell = best_cell

    return limiter
