# Python-Vocabulary-Word-Finder
This program can search a database of vocabulary words by the word itself, type (part of speech), or a word in its meaning. It can also add and remove words. 

# Try it out on Repl.it: https://repl.it/@lk101/Vocabulary-Word-Finder

**Requirements:** Python 2.7 and a CSV file (see example vocab.csv file)

## 1. Users can search for vocabulary words in a CSV file. 
They can search by the word itself, the type of word (part of speech such as noun, adjective, adverb, etc.) or by a word in the definition. Every row that matches the query is returned. 

#### search queries can be
   - **word** : returns entire row of that word
        - input example:    word, querulous
   - **type** : adjective, noun, adverb, verb: returns all rows of words that match type
        - input example:    type, adjective
   - **word that matches 'meaning' column**: returns all rows of words that have word
        - input example:    meaning, complaining
        
        All of these examples would return the row
        - querulous, adjective, full of complaints; complaining in an annoyed way

## 2. Users can add their own words to a CSV file.
Use the format | word, type, definition |. Add words in bulk or choose 'quit' to exit the program. Fill in at least 3 columns to use the search feature. 

#### Note:
Since CSV files are separated by commas, a definition with commas will create new columns. **Do not put any spaces after a comma when adding rows.** The search function for the meaning column can separate words from semicolons, commas, and other symbols. 

## 3. Users can remove selected words from the file and the remaining rows will be written in a new file.

## 4. Users can return a random word row from a non-empty CSV file.
