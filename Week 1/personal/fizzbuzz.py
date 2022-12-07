#program details:
#divisible by 3, print fizz
#divisible by 5, print buzz
#divisible by 3 and 5, print fizzbuzz
#not divisible, print number

#program details:
#1. loops
#2. if, elif, else

for i in range(1,100):
    if i % 5 == 0 and i % 3 ==0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)