#problem set ver. 1 (i will always just do ver. 1 for all units & sessions)
def hello_world():
    print("Hello world")
hello_world()

def todays_mood():
    mood = "happy"
    print("Today's mood: " + mood)
todays_mood()

def print_menu(menu):
    print("Lunch today is: " + menu)  
print_menu("pizza")

def sum(a, b):
    return a + b
sum(13, 27)
print(sum(sum(13, 27), sum(13,27)))

def product(a, b):
    return a * b

def classify_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"   
output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)

def what_time_is_it(hour):
    if hour == 2:
        return "taco time"
    elif hour == 12:
        return "peanut butter jelly time"
    else:
        return "nap time"        
time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)


def get_first(lst):
    if len(lst) == 0:
        return "none"
    else:
        return lst[0]

def get_last(lst):
    if len(lst) == 0:
        return "none"
    else: return lst[len(lst)-1]
    
def counter(stop):
    current = 1
    while current <= stop:
        print(current)
        current += 1
counter(10)

def sum_positive_range(stop):
    current = 1
    sum = 0
    while current <= stop:
        sum = sum + current
        current += 1
    print(sum)
sum_positive_range(6)

def sum_range(start, stop):
    current = start
    sum = 0
    while current <= stop:
        sum = sum + current
        current += 1
    print(sum)
sum_range(3, 9)

def print_negatives(lst):
    for i in range(len(lst)):
        if (lst[i] < 0):
            print(lst[i])
print_negatives([3,-2,2,1,-5])
