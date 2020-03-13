import json
import time
import sys                                      #used for exiting program
from difflib import get_close_matches           #library to compare text

data = json.load(open("data.json"))

while True:
    def translate(word):
        word = word.lower()                     #takes input and converts it to lowercase in order to search dictionary
        if word == ".exit":                     #exits if command true
            sys.exit()

        if word in data:                        #searches for words in lowercase
            return(data[word])

        elif word.title() in data:              #searches for title words in dictionary
            return data[word.title()]

        elif word.upper() in data:              #searches for acronyms in words dictionary
            return data[word.upper()] 

        elif len(get_close_matches(word, data.keys())) > 0:         #only executes code if something has been typed else returns "word not in dictionary"
            yn = input("Did you mean %s instead? Enter 'Y' if yes or 'N' if not: " % get_close_matches(word, data.keys())[0])
            yn = yn.upper()                        #takes user input and convert to uppercase in order to match with required response

            if yn == "Y":
                return data[get_close_matches(word, data.keys())[0]]

            elif yn == "N":
                return "Word does not exist in dictionary!"

            else:
                return "Request not completed!"

        else:
            return("word not in dictionary")

    user_word = input(" search dictionary\n or type '.exit' to exit dictionary\n -> ")
    output = translate(user_word)

    if type(output) == list:
        for item in output:            #outputs values of item in list
            print(item)
    else:
        print(output)               #outputs correctly our prompts
    time.sleep(10)