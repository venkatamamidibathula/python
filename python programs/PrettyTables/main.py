from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["City", "Population", "Area"]
x.add_rows([["Irvine", int(300000), int(785)], ["Sacramento", int(650000), int(900)]])
print(x)
