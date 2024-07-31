import numpy as np

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(
    the_first_number_to_multiply_this_is_a_long_name_for_a_variable,
    the_second_number_to_multiply,
):
    """This funcation takes two numbers a and b and multiplies them."""
    return (
        the_first_number_to_multiply_this_is_a_long_name_for_a_variable
        * the_second_number_to_multiply
    )

def mean(numbers):
    return np.mean(numbers)


numbers = [1, 2, 3]
print(mean(numbers))
print(add(10, 5))
