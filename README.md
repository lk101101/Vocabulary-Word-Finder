# Python-Vocabulary-Word-Finder

When I'm writing, I sometimes forget the exact word I need at that moment. I might remember the word, but not the meaning, or vice versa. To find the word, I would search through my Google Doc of 800+ vocab words, which is time-consuming and inefficient. I realized that I could code a more practical way to sort through my vocab words. 


## 1. Users can search for vocabulary words in a CSV file by choosing 's'. 
They can decide which criteria: the word itself, the type of word (noun, adjective, adverb, etc.) or by a word in the definition. Every row that is matched with the query is returned. Each word in the definition column is a separate string. 

#### search queries can be
   - **word** : returns entire row of that word
        - input example:    word, querulous
   - **type** : adjective, noun, adverb, verb: returns all rows of words that match type
        - input example:    type, adjective
   - **word that matches 'meaning' column**: returns all rows of words that have word
        - input example:    meaning, complaining
        
        All of these examples would return the row
        - querulous, adjective, full of complaints; complaining in an annoyed way

## 2. Users can add their own words to the CSV file by choosing 'a'. 
Use the format | word, type, meaning of the word |. Users have the option to add words in bulk or choose 'quit' to exit the program. 

### Note:
The rows are separated by commas, so a definition with commas will create new columns. Instead, do not put any spaces after a comma. The search function for the meaning column can separate words from semicolons, commas, etc. 

## 3. Users can remove selected words from the file and the remaining rows will be written in a new file.

## 4. Users can return a random word row by choosing 'w'.

This program is very simple, so with minor changes, it could organize music libraries or track spending. I have included an example vocab.csv file for testing. 
