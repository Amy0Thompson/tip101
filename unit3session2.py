# def reverse_only_letters(s: str):
#     # STEP 1
#     save_indexes = []
#     for index, char in enumerate(s):
#         if char == '-':
#             save_indexes.append(index)
#     print(save_indexes)
#     # STEP 2
#     lst_revers = s.split('-')[::-1]
#     new_list = []
#     for word in lst_revers:
#         new_list.append(word[::-1])
#     # STEP 3
#     reversed_str = ''.join(new_list)
#     print(reversed_str)
#     # STEP 4
#     letters_pointer = 0
#     empty_str = ''
#     for i in range(len(s)):
#         if i in save_indexes:
#             empty_str += '-'
#         else:
#             empty_str += reversed_str[letters_pointer]
#             letters_pointer += 1
#     return empty_str
# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s)
# # j-Ih-gfE-dCba
#problem we were stuck on ^^