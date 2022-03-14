## list comprehension ##
### new_list = [new_item for item in list] ###

numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)


new_list = [n+1 for n in numbers]
print(new_list)


### conditional list comprehension ###
### new_list = [new_item for item in list if test] ###

new_even = [ n for n in range(1,20) if n%2 == 0]
print(new_even)

names = ["Ashish","Ishant","pratham","Priyank"]
caps_6_letter_names = [name.upper() for name in names if len(name) <= 6]
print(caps_6_letter_names)