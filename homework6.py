string = raw_input("Search string: ")
character = raw_input("Search character: ")

count = 0
for c in string :
    if c == character:
        count = count +1
print "Found", count, character, "characters in string", string