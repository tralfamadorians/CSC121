"""3-10. Every Function: Think of things you could store in a list. For example, you
could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items and
then uses each function introduced in this chapter at least once."""

ncRivers = ["french broad river", "mills river", "green river", "swannanoa river"]

print(ncRivers)
print(ncRivers[1])
print(ncRivers[-1])
print(f"The {ncRivers[0].title()} is the third oldest river in the world.")

ncRivers[2] = 'pigeon river'
print(ncRivers[2])

ncRivers.append('green river')
print(ncRivers)
ncRivers.insert(3, 'catawba river')
print(ncRivers)

del ncRivers[5]
print(ncRivers)
first = ncRivers.pop(0)
print(f"The {first.title()} is now removed from the list.")

ncRivers.remove('mills river')
print(ncRivers)

print(sorted(ncRivers))
print(ncRivers)

ncRivers.reverse()
print(ncRivers)

ncRivers.sort()
print(ncRivers)
ncRivers.sort(reverse=True)
print(ncRivers)

print(f"The length of this list is {len(ncRivers)}.")