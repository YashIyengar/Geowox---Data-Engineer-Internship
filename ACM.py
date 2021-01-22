from math import copysign
import re

def tragedy_to_comedy():
    """
    Method Name: tragedy_to_comedy
    Description: This method accepts the tragedy inputs, adds them and reverses the output so that it can be converted into comedy
    Output: casewise reversed sum of the inputs
    On Failure: Raise ValueError,Exception

    Written By: Yash Iyengar
    Written On: 21-01-2021
    Version: 1.0
    Revisions: None

    """
    try:
        cases = int(input("Please Enter the number of cases:"))                       # This line of code accepts user input for total number of cases.

        if copysign(1,cases)==-1:                                                     # This condition checks if the sign of the number of cases entered is negative.
            print("Number of Cases can't be Negative")
        elif cases==0:                                                                # This condition checks if the number of cases entered is zero.
            print("Number of Cases can't be Zero")
        else:
            pass
    except ValueError:
        print("Number of Cases can't be non-integer")
    except Exception as e:
        print(e)
    else:
        for i in range(cases):
            try:
                a,b = input("Please Enter 2 integers separated by a space:").split()  # This line of code accepts user input for two integers and assigns them to two variables .
                a = re.sub("^0+(?!$)", "", a)                                         # This regex pattern checks for any preceeding zeros for the inputed number.
                b = re.sub("^0+(?!$)", "", b)
            except ValueError:
                print("Input numbers were not integers")
            except Exception as e:
                print(e)
            else:
                try:
                    print(int(str(int(a[::-1])+int(b[::-1]))[::-1]))                  # This line of code performs addition of the two reversed numbers and then reverses the sum and print's it.
                except ValueError:
                    print("Input numbers were not integers")


if __name__ == "__main__":
    tragedy_to_comedy()