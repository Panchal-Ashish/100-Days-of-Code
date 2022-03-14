### READING THE FILE ###

## 1.requires manual closing... However if the file remains open, no issue

# file = open("demo_file.txt")
# contents = file.read()
# print(contents)
# file.close()

## 2.automatic file closing
# with open("demo_file.txt") as file:
#     contents = file.read()
#     print(contents)




### WRITING IN THE FILE ###

## 1.erases everything previously written in the file
# with open("demo_file.txt",mode = "w") as file:
## by default, the mode is read only ("r")... changing to it write mode("w")
#     contents = file.write("new text")

## 2.do not delete previously written text, instead add to it
with open("demo_file.txt", mode= "a") as file:      # changing mode to append ("a")
    file.write("\nnew text")


## Note if we use write method for a file that does not exist, it will create a new file for us
with open("xyz file.txt",mode= "w") as file:
    file.write("new xyz text")


