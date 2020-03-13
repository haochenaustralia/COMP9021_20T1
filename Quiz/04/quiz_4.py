# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


from math import sqrt
from itertools import permutations


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    # Only used to test odd numbers.
    return all(n % d for d in range(3, round(n ** 0.5) + 1, 2))


def first_sieve_of_primes_up_to(n):
    sieve = list(range(2, n + 1))
    i = 0
    while sieve[i] <= round(sqrt(n)):
        k = 0
        while True:
            factor = sieve[i] * sieve[i + k]
            if factor > n:
                break
            while factor <= n:
                sieve.remove(factor)
                factor *= sieve[i]
            k += 1
        i += 1
    return sieve


def second_sieve_of_primes_up_to(n):
    sieve = list(range(2, n + 1))
    i = 0
    while sieve[i] <= round(sqrt(n)):
        sieve_as_set = set(sieve)
        k = 0
        while True:
            factor = sieve[i] * sieve[i + k]
            if factor > n:
                break
            sieve_as_set.remove(factor)
            k += 1
        sieve = sorted(sieve_as_set)
        i += 1
    return sieve


# 没有0，数字不重复，素数
# A number is a good prime if it is prime and consists of nothing but
# distinct nonzero digits.
# Returns True or False depending on whether the integer provided as
# argument is or is not a good prime, respectively.
# Will be tested with for number a positive integer at most equal to
# 10_000_000.
def is_good_prime(number):
    # REPLACE PASS ABOVE WITH YOUR CODE
    # if str(number).count('0') > 0 or len(set(str(number))) != len(str(number)):
    # 没有0，数字不重复，素数
    return False if '0' in str(number) or len(set(str(number))) != len(str(number)) else is_prime(number)


# pattern is expected to be a nonempty string consisting of underscores
# and digits of length at most 7.
# Underscores have to be replaced by digits so that the resulting number
# is the smallest good prime, in case it exists.
# The function returns that number if it exists, None otherwise.
def smallest_good_prime(pattern):
    # REPLACE PASS ABOVE WITH YOUR CODE
    # 没有0，数字不重复，最小的good素数
    result = None
    if '0' in pattern:
        return result
    # check完整的数字
    if '_' not in pattern:
        if is_good_prime(int(pattern)):
            result = int(pattern)
        return result

    # check重复的数字
    # 是否存在重复的数据
    #
    if [1 for item in pattern if item != '_' and pattern.count(item) > 1]:
        return None

    all_digits = list('123456789')
    pattern_digits = set(pattern.replace('_', ''))

    # _12_  3456789
    # 3124
    # 4123
    pattern_left_digits = list(sorted(set(all_digits) - pattern_digits))
    # 2
    underscore_count = pattern.count("_")
    permutations_result = permutations(pattern_left_digits, underscore_count)
    for items in permutations_result:
        number = get_number_by_items(pattern, items)
        if is_good_prime(number):
            print(pattern, number)
            return number
    return None


# POSSIBLY DEFINE OTHER FUNCTIONS
def get_number_by_items(pattern, items):
    pattern_list = list(pattern)
    index = 0
    for underscore_index in range(len(pattern_list)):
        if pattern_list[underscore_index] == '_':
            pattern_list[underscore_index] = items[index]
            index += 1
    # 执行完for循环之后
    # pattern_list = ['3','1','2','4']
    number = int("".join(pattern_list))
    return number


if __name__ == "__main__":
    smallest_good_prime('_0_')
    smallest_good_prime('2_2')
    smallest_good_prime('123')
    smallest_good_prime('_98')
    smallest_good_prime('3167')
    smallest_good_prime('__')
    smallest_good_prime('___')
    smallest_good_prime('1_7')
    smallest_good_prime('_89')
    smallest_good_prime('_89_')
    smallest_good_prime('_2_4_')
    smallest_good_prime('1__4_7')
