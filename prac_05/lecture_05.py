"""
Lecture 5, Week 5

Dictionary and Sets

.index()
    used to find the index of that point inside a list
    usually used when there is two lists corresponding to each other

for i, age in enumerate(ages)
    when you want to track the both index and the single object

dictionary {}
    dictionary = {key:value, key:value}
    key value map
    collection of key value pairs
    used when data has a relationship between key and value
        key = immutable, lists are not allowed
        value = can be anything
    dictionary itself is a mutable objects
    name is done using the two dataset
        key_to_value
        example: name_to_age

how to use dictionary
    add new value
        dictionary[key] = value
        if key exists in the dictionary, the value associated will be changed
    remove/delete
        del dictionary[key]
        if there is no key, KeyError will occur
    replace key with the same value
        dictionary[new_key] = dictionary.pop(old_key)

dictionary content methods
    .keys()
        shows all the keys present
    .values()
        shows all the values
    .items()
        shows all the key/value pairs as a tuple
    .get()
        returns the value of a key
        if the key didn't exist, it returns the second argument
        it will not make the KeyError occur\
            word_to_count.get(word,0) + 1

    these methods can make those keys/values into a list but these lists are dynamic
        if the original dictionary is modified, the change will also affect the created lists

for loops for dictionary
    dictionary will use the key as an index when it's applied into a for loop
    to get the both key and value into a for loop, use .item()
        for key, value in dict.item()
    this will return a tuple contain both the key and the value

set() {}
    it is a set of data without duplication
"""

# Write code for a function that takes two lists: a list of names, and a corresponding list of ages.
# Elements at the same list index represent the same person. The function will return the name of the oldest person in the list.
# If multiple people have the same oldest age, return the first name.

# names = ["Alex", "Ben", "Caley", "Dwain"]
# ages = [21, 20, 27, 40]
#
# oldest_age = max(ages)
# oldest_person = names[ages.index(max(ages))]
# print(f"The oldest person is {oldest_person} with the age {oldest_age:.0f}.")

# Write a code to prompt the user for a new name and age
# add these to the dict, then display all the data nicely

name_to_age = {"Bill": 21, "Jane": 4, "Sven": 56}

name = input("Name: ")
age = int(input("Age: "))
name_to_age[name] = age
longest_name = max(len(name) for name in list(name_to_age.keys()))
for name, age in name_to_age.items():
    print(f"{name:{longest_name}} - {age:>5}")


