# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: define the 'PREPARATION_TIME' constant
EXPECTED_BAKE_TIME = 40


# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(actual_mins_in_oven):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - actual_mins_in_oven


bake_time_remaining(10)

# TODO: define the 'preparation_time_in_minutes()' function

# TODO: define the 'elapsed_time_in_minutes()' function
