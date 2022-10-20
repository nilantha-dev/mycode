#!/usr/bin/python3
"""Alta3 Research | nilantha challenge lists, input, concatenation"""

# import random module
import random

def main():

    # enter variable data
    wordbank= ["indentation", "spaces"]
    tlgstudents= ["Aaron", "Andy", "Asif",
            "Brent", "Cedric", "Chris",
            "Cory", "Ebrima", "Franco",
            "Greg", "Hoon", "Joey",
            "Jordan", "JC", "LB",
            "Mabel", "Shon", "Pat", "Zach"]
    # print the tlg list as shown above. This helps to compare differences later implemented.
    # append the integer 4 to the wordbank list and then print the new list
    wordbank.append(4)
    print(wordbank)

    # for Bonus 2. Student name printed out below is related to input from user.
    num = int(input(f"Enter a student number between 1 and {len(tlgstudents)} --> "))-1
    name = tlgstudents[num]

    print(f"Your unfortunate victim is {name}!")
    #print here is pulling variable data from wordbank list as well as 'name' set above
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")

    # for Bonus 1, from the random library, .choice is used to pick a random student name and printed out
    name = random.choice(tlgstudents)
    print(f"{name}")

if __name__ == "__main__":

main()

