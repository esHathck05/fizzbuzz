#fizzbuzz.py
#Author: Esther Hacker
#Credit: N/A

#Assignment: FizzBuzz

for i in range(1, 101):
    if i in range(0, 101, 3) and i in range(0, 101, 5):
        print("fizzbuzz")
    else:
        if i in range(0, 101, 3):
            print("fizz")
        else:
            if i in range(0, 101, 5):
                print("buzz")
            else:
                    print(i)
