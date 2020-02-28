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
    return values.index(x)

    # 6

def length_of_cycle_containing(values, x):
    # pass
    # REPLACE PASS ABOVE WITH YOUR CODE
    cycle_values = [x]

    # x = maps_to(values, x)
    x = values.index(x)

    while x not in cycle_values:
        cycle_values.append(x)
        # x = maps_to(values, x)
        x = values.index(x)

    return len(cycle_values)








# Returns a list of length len(values) + 1, with 0 at index 0
# and for all x in {1, ..., len(values)}, the length of the cycle
# containing x at index x.
def analyse(values):
    # pass
    # REPLACE PASS ABOVE WITH YOUR CODE
    # 没考虑性能，请注意！！！
    # 如果不调用上上面的方法的话，是可以优化性能的
    # result = [length_of_cycle_containing(values, x) for x in values]
    # result.insert(0, 0)
    # return result

    map_values = {value: index for index, value in enumerate(values, start=1)}

    while map_values:
        value, index = map_values.popitem()

        cycle_values = set()
        cycle_values.add(value)
        cycle_values.add(index)

        while index in map_values:
            index = map_values.pop(index)
            cycle_values.add(index)

        length = len(cycle_values)
        for item in cycle_values:
            values[item - 1] = length

    return values


if __name__ == "__main__":
    values = generate_permutation(1, 10_000_000)
    cycle_lengths = analyse(values)
    print(len(cycle_lengths))
    print(cycle_lengths[500])
    # values = generate_permutation(2, 1000)
    # cycle_lengths = analyse(values)
    # print(cycle_lengths)
    # print(len(cycle_lengths))
    # print(cycle_lengths[500])
