def all_in(a, b):
    for i in a:
        if i not in b:
            return False
        else:
            return True
lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1)) #TODO should return false but isnt

#TODO we worked on problems in breakout rooms. just did to add the solutions here