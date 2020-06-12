from __future__ import print_function
import csv
import codecs
import random
import re

print(" ")
print("Welcome to Vocab Finder! Please select an option from the menu below: \n")
print("Search vocabulary (s)", "Add word (a)", "Remove word (r)", "Random word (w)", sep='\n')
choice = raw_input("")

# REQUIRES: Search query is written in format (search type, word) and file is not empty
# EFFECTS: Returns row that matches word/type/meaning from search query
if choice.lower() == "s":
    search_parts = raw_input("Enter search criteria (type, word, meaning) in format (search type, word): \n").split(", ")
    with open('vocab.csv') as csvfile:
        reader = csv.reader(codecs.EncodedFile(csvfile, 'utf8', 'utf_8_sig'))
        count = 0

        def errorMessage():
            print("No results matched your search.")

        for row in reader:
            
            def updateCount():
                global count
                count += 1
            # function to print each row without list brackets
            def printRows():
                newRow = str(row)[1:-1]
                print(newRow + '\n')
                updateCount()


            if search_parts[0].lower() == "type" and search_parts[1].lower() == row[1]:
                    printRows()

            # check word columns for specific word
            elif search_parts[0].lower() == "word" and search_parts[1].lower() == row[0]:
                    printRows()

            # check meaning column for specific word
            elif search_parts[0].lower() == "meaning":
                # ensures that word can be matched even w/ semicolons, commas, etc.
                if search_parts[1].lower() in re.split('[;,.\-\%, ]', row[2]):
                    printRows()

        # no results for search
        if count == 0:
            errorMessage()
           
        print("Number of results found:", count)


#EFFECTS: adds row to file
#MODIFIES: original CSV file
# loop allows user to add words in bulk and quit when completed
elif choice.lower() == "a":
    # use bool to loop through adding rows until user chooses to quit
    loop = True
    while loop:
        # split input by commas
        add_row = raw_input("Enter a new word using format | word, type, meaning | or quit: \n").split(", ")
        
        # end loop, quit program
        if add_row[0] == "quit":
            print("Finished adding words.")
            loop = False;
        else:
            # appends new row(s) to end of file
            with open('vocab.csv', 'a+') as f:
                writer = csv.writer(f)
                writer.writerow(add_row)

            with open('vocab.csv') as f:
                print(f.read())

    # enter as word, type, data

#REQUIRES: CSV file must not be empty
#EFFECTS: Returns a random row
elif choice.lower() == "w":
    with open('vocab.csv', 'rb') as f:
        reader = csv.reader(codecs.EncodedFile(f, 'utf8', 'utf_8_sig'))
        lines = [line for line in reader]
        random_choice = str(random.sample(lines, 1))[1:-1]
        print(random_choice)

#REQUIRES: CSV file must not be empty
#EFFECTS: Removes a selected row from file
#MODIFIES: A new CSV file filled with remaining words
elif choice.lower() == "r":
    loop = True
    remove_row = raw_input("Enter word that you want to remove: \n")
    updatedlist = []
    while loop:
        with open('vocab.csv', 'r+') as csvfile, open('vocab_new.csv', 'wb') as output:
            reader = csv.reader(codecs.EncodedFile(csvfile, 'utf8', 'utf_8_sig'))
            writer = csv.writer(output)
            for row in reader:
                # only consider words that are not the removed word
                if remove_row != row[0]:
                    updatedlist.append(row)
                    # adds remaining words to a new CSV file
                    with open("vocab_new.csv","w") as f:
                        writer = csv.writer(f)
                        writer.writerows(updatedlist)
                        loop = False
