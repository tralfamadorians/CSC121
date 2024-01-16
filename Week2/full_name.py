first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)

print("python")
print("\tpython")

print("Languages: \nPython\nJavascript\nRuby")

fav = 'python '
print(fav + '*')
print(fav.rstrip() + ".")

long = "  here it is  "
print("." + long + ".")
short = long.strip()
print("." + short + ".")