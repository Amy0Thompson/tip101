def hello_world():
    print("Hello world")
hello_world()

def todays_mood():
    mood = "happy"
    print("Today's mood: " + mood)
todays_mood()

def print_menu(menu):
    menu = "pizza"
    print("Lunch today is: " + menu)

def sum(a, b):
    return a + b
sum(13, 27)
sum(sum(13, 27), sum(13,27))

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

output = classify_age(18)
print (output)
output = classify_age(7)
print (output)
output = classify_age(50)
print (output)

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

#test