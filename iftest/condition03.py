#!/usr/bin/env python3
# Alta3 Research || Author: RZFeeser@alta3.com
#Check hostname against expected value

##Collect input from user
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

## Always print out to the user
print("Exiting the script")

