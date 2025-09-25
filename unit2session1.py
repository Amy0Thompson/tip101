def all_in(a, b):
    for i in a:
        if i not in b:
            return False
    return True
lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1)) 

def create_dictionary(keys, values): 
    d = {}
    for i in range (len(keys)):
        d[keys[i]] = values[i]
    return d
keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']
print(create_dictionary(keys, values))

def print_pair(dictionary, target):
    if target in dictionary:
            print("Key: " + target)
            print("Value: " + dictionary.get(target)) 
    else:
        print("That pair does not exist!")
dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")



#TODO we worked on problems in breakout rooms. just need* to add the solutions here