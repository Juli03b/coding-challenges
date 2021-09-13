def fizzBuzz(n: int):
    """
    - FizzBuzz if i is multiple of 3 & 5
    - Fizz if i is a multiple of 3 but not 5
    - Buzz if i is a multiple of 5 but not 3
    - Else print i
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        else:
            print(i)

print(fizzBuzz(8))