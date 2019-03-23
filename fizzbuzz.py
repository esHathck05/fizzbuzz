#fizzbuzz.py
#Author: Esther Hacker
#Credit: N/A

#Assignment: FizzBuzz

number = int(input("How many numbers shall we print? ")) + 1
fizznumber = int(input("For multiples of what number shall we print 'Fizz'? "))
buzznumber = int(input("For multiples of what number shall we print 'Buzz'? "))

for i in range(1, number):
    if i in range(0, number, fizznumber) and i in range(0, number, buzznumber):
        print("FizzBuzz")
    else:
        if i in range(0, number, fizznumber):
            print("Fizz")
        else:
            if i in range(0, number, buzznumber):
                print("Buzz")
            else:
                    print(i)
