for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBizz")
    elif  num % 5 == 0:
        print("Biz")
    elif num % 3 == 0 :
        print("Fizz")
    else:
        print(num)
