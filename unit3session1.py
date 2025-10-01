def compress_string(my_str):
    counter = 1
    returnString = ""
    for i in range(1, len(my_str)):
        if my_str[i] == my_str[i - 1]:
            counter += 1
        else:
            returnString += my_str[i-1] + str(counter)
            counter = 1
    return returnString
#expected: a5b2c3d1 & abcde 

# def compress_string(my_str):
#     counter = 0
#     returnString = ""
#     for char in my_str:
#             for char in range(1, len(my_str)):
#                 if my_str[char + 1]  != None:
#                     if my_str[char] == my_str[char + 1]:
#                         counter += 1
#                         returnString += my_str[char] + str(counter)
    
my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2)

                
                    


#another for loop
#maybe using a for loop 
#if my_str[i] == my_str[i + 1]
# index 0: a & index 1: a
#counter++
#returnString += "my_str[i]" + "2"
