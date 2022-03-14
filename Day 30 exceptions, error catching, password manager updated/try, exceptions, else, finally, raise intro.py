try:        # does not give any error even if present... instead, checks for exemption
    file = open("a.file.txt")
    a_dict = {"key":"Value"}
    print(a_dict["sdvsx"])

except FileNotFoundError:   # executes if try stmt fails    # if err type is not specified, it considers all the errors that occur and executes this stmt
    # here the file does not exist, so it creates the new file
    file = open("a.file.txt", "w")
    file.write("Something")

except KeyError as err_msg:     # we can also catch the error, show our own err notice
    # If we give a key that does not exist, then at this pt, file is already created, but key does not exist
    print(f"The key {err_msg} does not exist")

else:       # executes only if try stmt is fully executed (ie. exemptions are false)
    # in except stmt, file is created so when run again, it writes (as per try stmt) and we can read that in else stmt
    content = file.read()
    print(content)

finally:    # executes under all circumstances
    print("Finally command executed")




# RAISE - creating our own exemptions ##
# if your code is perfectly valid... but you want to put some limits

ht = float(input("Enter your Height (in metres): "))
wt = float(input("Enter your Weight (in kg): "))

if ht > 2.5:
    raise ValueError("Human height cannot exceed 2.5 metres")

bmi = wt / ht**2
print(bmi)