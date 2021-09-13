from typing import Set

def frequencyCounter(str: str) -> Set:
    frequencies = dict()

    for char in str:
        count = frequencies.get(char, 1)
        frequencies[char] = count + 1

    return frequencies
def validAnagram(str1: str, str2: str) -> bool:
    """
    Given two strings, write a function called validAnagram, which determines 
     if the second string is an anagram of the first. An anagram is a word, phrase,
     or name formed by rearranging the letters of another, such as cinema, formed from iceman.
    """
    if len(str1) is not len(str2): return False
    
    str1_freq = frequencyCounter(str1)
    str2_freq = frequencyCounter(str2)

    for char in str1:
        if str1_freq[char] is not str2_freq[char]:
            return False

    return True

print(validAnagram("aaz", "zza")) # False
print(validAnagram("anagram", "nagaram")) # True
print(validAnagram("qwerty", "qeywrt")) # True