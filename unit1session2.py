def print_list(list):
    for i in list:
        print(i)
lst = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(lst)

def doubled(list):
    for i in list:
        print(i * 2)
lst = [1,2,3]
doubled(lst)

def doubled2(list):
    doubleNumbers = []
    for i in list:
        doubleNumbers.append(i * 2)
    return doubleNumbers
lst = [1,2,3]
print(doubled2(lst))

def flip_sign(list):
    flippedNumbers = []
    for i in list:
        flippedNumbers.append(i *-1)
    return flippedNumbers
lst = [1,2,3]
print(flip_sign(lst))

def max_difference(lst):
    if len(lst) < 1:
        return 0 
    maxNum = max(lst)
    minNum = min(lst)
    return maxNum - minNum
print(max_difference([5,22,8,10,2]))

def count_less_than(lst, threshold):
    counter = 0
    for i in lst:
        if (i < threshold):
            counter += 1
    return counter
numbers = [12,8,2,4,4,10]
count = count_less_than(numbers,5)
print(count)

def get_evens(lst): 
    even = []
    for i in lst:
        if i % 2 == 0:
            even.append(i)
    return even
lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)

def multiples_of_five():
    for i in range(5, 101, 5):
        print(i)
multiples_of_five()

def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
lst = find_divisors(6)
print(lst)

def fizzbuzz(n):
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif (i % 5 == 0):
            print("Buzz")
        elif (i%3 == 0):
            print("Fizz")
        else:
            print(i)
fizzbuzz(15)

def print_indices(lst):
    for i in range(len(lst)):
        print(i)
lst = [5,1,3,8,2]
print_indices(lst)

def linear_search(lst, target):
    for i in range(len(lst)):
        if (lst[i] == target):
            return i
    return -1
lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)
#my breakout group also did some questions in the second set



    
        

    
            
            

            
    

