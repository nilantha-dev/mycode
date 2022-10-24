#!/usr/bin/env python3

book= open("dracula.txt","r") #Read in the content of the Dracula novel as a file object.
outFile= open("vampytimes.txt", "w")
#Loop over every line in Dracula, print each line out, if the word vampire in it!
count=0
for line in book:
    if "vampire" in line.lower():
        print(line)
        count += 1 # Count that up! How many times does the word vampire appear?
        print(line, file=outFile) #Take the lines from Dracula that have vampire in it and write them to a second file
print(count)
book.close()
outFile.close()
