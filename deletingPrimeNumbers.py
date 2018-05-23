# Delete all prime numbers from the first halfe part of integer sequence
import math


def delete_first_half_prime_numbers(sequence):
    def prime(x):
        for j in range(2, int(math.sqrt(x)) + 1):
            if x % j == 0:
                return False
        return True

    for i in reversed(range(0, len(sequence) // 2)):
        if prime(sequence[i]):
            del sequence[i]
    return sequence


sequence = [1, 2, 3, 5, 6, 7, 8, 11, 17, 19, 20, 21, 23, 25, 27, 30, 33, 35, 37, 40, 41]
print(delete_first_half_prime_numbers(sequence))
