# Written by *** and Eric Martin for COMP9021


from random import seed, shuffle
import sys


# for_seed is meant to be an integer, length a strictly positive integer.
# length will not be large for most tests, but can be as large as 10_000_000.
def generate_permutation(for_seed, length):
    seed(for_seed)
    values = list(range(1, length + 1))
    shuffle(values)
    return values


def maps_to(values, x):
    # pass
    # REPLACE PASS ABOVE WITH YOUR CODE
    #
    # values.index(x)
    # values.find(x)

    for index in range(len(values)):
        if values[index] == x:
            return index + 1
    return -1



def length_of_cycle_containing(values, x):
    # pass
    # REPLACE PASS ABOVE WITH YOUR CODE
    cycle_values = [x]
    x = maps_to(values, x)
    while x not in cycle_values:
        cycle_values.append(x)
        x = maps_to(values, x)
    return len(cycle_values)


# Returns a list of length len(values) + 1, with 0 at index 0
# and for all x in {1, ..., len(values)}, the length of the cycle
# containing x at index x.
def analyse(values):
    # pass
    # REPLACE PASS ABOVE WITH YOUR CODE
    # 没考虑性能，请注意！！！
    # 如果不调用上上面的方法的话，是可以优化性能的
    result = [length_of_cycle_containing(values, x) for x in values]
    result.insert(0, 0)
    return result
