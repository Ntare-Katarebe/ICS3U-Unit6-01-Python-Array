#!/usr/bin/env python3

# Created by: Ntare-Katarebe
# Created on: June 2021
# This program uses an array(list)

import math
import random


def main():
    # this function uses an array

    my_numbers = []
    sum_of_all_numbers = 0

    # input
    for loop_counter in range(0, 10):
        a_single_number = random.randint(1, 101)
        my_numbers.append(a_single_number)
        print("The random is: {0}".
              format(my_numbers[loop_counter]), end="\n")
    print("")

    for loop_counter in range(0, len(my_numbers)):
        sum_of_all_numbers = sum_of_all_numbers + my_numbers[loop_counter]
        average = sum_of_all_numbers / len(my_numbers)
        print("The average is: {0}".format(average))
        print("\nDone.")


if __name__ == "__main__":
    main()
