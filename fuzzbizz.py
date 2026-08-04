for num in range(1,16):
    if num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 3 != 0 and num % 5 == 0:
        print("Buzz")
    elif num % 3 ==0 and num % 5 == 0:
        print("Fizz Buzz")
    else:
        print(num)            