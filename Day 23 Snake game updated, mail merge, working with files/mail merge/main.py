#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp




PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:     # accessing names from invite list
    names = names_file.readlines()          # reads all lines from txt file and saves each line in the form of string inside a list
    print(names)



## using absolute path
# with open("/Users/Manoj/Desktop/programing/udemy 100 days of code/"
#           "Day 24 snake game updated(highscore),mail merge, working with files/Day 24 mail merge"
#           "/Mail Merge Project Start/Input/Letters/starting_letter.txt") as start_letter:
#     letter_contents = start_letter.read()
#     print(letter_contents)

## Using relative path
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    print(letter_contents)

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)

        ## Using Absolute path
        # with open(f"/Users/Manoj/Desktop/programing/udemy 100 days of code/"
        #         f"Day 24 snake game updated(highscore),mail merge, working with files/Day 24 mail merge/"
        #         f"Mail Merge Project Start/Output/ReadyToSend/letter for {stripped_name}.txt",mode="w") as complete_letter:


        ## Using relative path
        with open(f"./Output/ReadyToSend/letter for {stripped_name}",mode="w") as complete_letter:
            complete_letter.write(new_letter)


