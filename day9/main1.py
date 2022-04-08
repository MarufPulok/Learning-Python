programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary)

#adding element in a dictionary

programming_dictionary["loop"] = "A loop is a piece of code that is repeated over and over again."

print(programming_dictionary)

#creating an empty dictionary
emptyDictionary = {}
print(emptyDictionary)

#wiping a dictionary
# programming_dictionary = {}
print(programming_dictionary)

programming_dictionary["Bug"] = "moth"
print(programming_dictionary)

for thing in programming_dictionary:
    print(thing)
    #this print statement only prints the keys
    print(programming_dictionary[thing]) #this prints the values