'''
Developer: @skywalkerSam
Purpose: A simple & strong password generator...
Date: 12022.09.23.04:32:00
'''

from logging import exception
import random as rd


# Password combinations
symbols_list = ['!', '#', '$', '%', '&', '^',
                '(', ')', '*', '+', '-', '.', ',', '<', '>', ':', ';', '=', '_', '[', ']', '{', '}', '"', "'"]
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def intro():
    print("""
                                                ###############################################
                                                        ***** Password Generator *****
                                                ###############################################
    """)


def password_generator():
    num_symbols = int(input("Number Of Symbols : "))
    num_letters = int(input("Number Of Letters : "))
    num_integers = int(input("Number Of Integers: "))
    # Integers List
    integers_list = []
    for i in range(num_integers):
        integers_list.append(i)

    symbols_one = rd.sample(symbols_list, num_symbols)
    letters_one = rd.sample(letters_list, num_letters)
    integers_one = rd.sample(integers_list, num_integers)
    password_one = symbols_one + letters_one + integers_one
    simple_password = "".join([str(c) for c in password_one])
    print(f"\n\t A Simple & Strong Password:  {simple_password}")
    pro_password = "".join(rd.sample(simple_password, len(simple_password)))
    print(f"\n\t A Pro Password:    {pro_password}\n\n")


if __name__ == "__main__":
    while True:
        try:
            intro()
            password_generator()
        except KeyboardInterrupt:
            print("\n\n\n\n\n\t\t\t Operation Cancelled By The User :( \n\n\n")
            break
        except ValueError:
            print(
                "\n\t Please Enter The Number OF \"Password Combinations\" Carefully ;) \n")
            print(
                f"\t\t>_ Maximum Combination Of Symbols: {len(symbols_list)}")
            print(
                f"\t\t>_ Maximum Combination of Alphabets: {len(letters_list)}")
            print(f"\t\t>_ 'Recommended' Combination of Positive Integers: 99 \n")
            continue
        except exception as e:
            # print(e)
            print("\n\t Something Went Wrong! Please Try Again :( \n\n")
            continue
