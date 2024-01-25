"""5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list"""

town = 'asheville'
print(town == 'boone')
print(town != 'boone')

year = 2024
print(year > 2000)
print(year >= 2024)
print(year < 2000)
print(year <= 2030)
print(year == 2024)
print(year != 2020)

if town == 'asheville' and year == 2024:
    print(f"Yes, it is the year {year} in {town.title()}")

if town == 'asheville' or town == 'boone':
    print("It's either Asheville or Boone.")

towns =['asheville', 'boone', 'highlands']
if 'asheville' in towns:
    print("Yes, Asheville is on the list.")
if 'hatteras' not in towns:
    print("No, Hatteras is not on the list.")

