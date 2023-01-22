#!/usr/bin/python3
for number in range(10):
    for number2 in range(number + 1, 10):
        if number == 4 and number2 == 5:
            print("{}{}".format(number, number2))
        else:
            print("{}{}".format(number, number2), end=", ")
