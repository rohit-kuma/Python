student = {"name" : "Rohit", "Age" : 30, "Courses" : ["Math", "Science"]}
student["Phone"] = 555555555
student["name"] = "Kumar"
student.update({"name":"jane", "Age": 26})
print(student)
print(student["name"])

#All the key can be any immutable data type
print(student.get("Age"))
print(student.get("gggg"))

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for keys, values in student.items():
    print(keys, values)
