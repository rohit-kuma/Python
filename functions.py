# def hello_fun():
#     print("Hello World")
#     return "rohit"
# hello_fun()
# print(hello_fun())
# rohit = "Rohit"
list1 = [11, 22, 33]
list2 = list1
greeting = 1
#Note: Greeting is call by value
# and list is call by reference
def hello_fun(greeting, list3):
    print(list3)
    list3[0] = 99
    greeting = 2
    print(f"{'greeting = '} {greeting}")
    print("greeting = ",greeting)
    return f"{greeting} {'Rohit'}"

list1[0] = 88
print(list2)
print(hello_fun("Hi", list2))
print(list1)
print(list2)
print(greeting)

num1 = 1
num2 = num1
num1 = 5
print(num1 is num2)

#Default Argument
def fun(num, val = 4):
    print(num, val)

#both having same result
fun(99, val = 8)
fun(99, 8)

def student(*args, **kwargs):
    print(args) #tuples
    print(kwargs) #dictionaries
# student("Art","Math","Eng",name="John",age="54",emp=6)

list1 = ["Art","Math","Eng"]
dict1 = {'name':"John",'age':"54",'emp':6}
# student(list1, dict1) #working as positional argument
student(*list1, **dict1)

print("###############################")

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]
