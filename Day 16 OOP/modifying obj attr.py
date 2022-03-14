from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","squirtle","Charmander"])
table.add_column("type",["electric","water","fire"])

# In this case, the first input is column heading, second heading are the items in the column

print(table)

table.align = "l"
print(table)
