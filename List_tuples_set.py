courses = ["history", "maths", "hindi"]
print(courses)
print(len(courses))
print(courses[1])
print(courses[-1])
print(courses[0:2])
courses.append("art")
courses.insert(1, "Geo")
courses2 = ["Art", "Education"]
print(courses)
#courses.insert(0, courses2)
#print(courses)
courses2.extend(courses)
print(courses2)
print(courses2.pop())
print(courses2)
courses2.remove("Geo")
print(courses2)
courses2.reverse()
print(courses2)
courses2.sort()
print(courses2)
num = [5, 1, 4]
num.sort(reverse=True)
print(num)
#without altering the original
num2 = sorted(num)
print(num2)
print(min(num2))
print(max(num2))
print(sum(num2))
print(num2.index(4))
print(4 in num2)
for i in courses2:
    print(i)

for index, courses in enumerate(courses2):
    print(index, courses)


for index, courses in enumerate(courses2, start = 1):
    print(index, courses)

courses_str = ", ".join(courses2)
print(courses_str)

new_list = courses_str.split(", ")
print(new_list)

#Tuples
#List are mutables tuples are not
# Mutable
print("Mutable List")
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)
list_1[0] = 'Art'


print(list_1)
print(list_2)

print("Immutable List")
# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)


print("Sets")
# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {"Math", "GEO", "Physics"}
print(cs_courses)
print(art_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()
