from typing import List

def mostFrequentDigits(nums: List[int]):
    """
    Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array. 
    Return the array of these digits in ascending order.
    
    Idea: 
        Create dictionary to map the intigers to a count of them. Then, loop through the numbers array and convert the intigers
        into strings, and add 1 to the count for that intiger in the dictionary. Loop through the keys of the dict and get the
        values that appear the most times.

    Example:

        For a = [25, 2, 3, 57, 38, 41], the output should be mostFrequentDigits(a) = [2, 3, 5]. Here are the number of times
         each digit appears in the array:

        0 -> 0
        1 -> 1
        2 -> 2
        3 -> 2
        4 -> 1
        5 -> 2
        6 -> 0
        7 -> 1
        8 -> 1

        The most number of times any number occurs in the array is 2, and the digits which appear 2 times are 2, 3 and 5.
        So the answer is [2, 3, 5].

    Input:
        An array of positive integers.
    
    Output:
        The array of most frequently occurring digits, sorted in ascending order.
    """
    get_count_by_digit = dict()
    highest_frequency_digits = []
    current_highest_digit_frequency = (0, 0)

    for num in nums:
        num = str(num)
        for num in num:
            digit_count = get_count_by_digit.get(num, 0) + 1
            get_count_by_digit[num] = digit_count
    for key in get_count_by_digit:
        frequency = get_count_by_digit[key]
        current_highest_frequency = current_highest_digit_frequency[1]
        if frequency > int(current_highest_frequency):
            current_highest_digit_frequency = (key, frequency)
        elif frequency == int(current_highest_digit_frequency[1]):
            highest_frequency_digits.append(key)
    if highest_frequency_digits:
        newarr = []
        for digit in highest_frequency_digits:
            frequency = get_count_by_digit[digit]
            if frequency >= current_highest_digit_frequency[1]:
                newarr.append(digit) 
        newarr.append(current_highest_digit_frequency[0])
        newarr.sort()
        if newarr: return newarr
    return [current_highest_digit_frequency[0]]
print(mostFrequentDigits([25, 2, 3, 57, 38, 41]))
# print(mostFrequentDigits([4, 5, 4, 2, 2, 25]))