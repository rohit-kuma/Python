
message = """Hello World"""
print(message)
print(len(message))
#for i in `len(message)`
#    print(message[i])
#Slicing
print(message[0:5])
print(message[:5])
print(message[6:])
print(message.lower())
print(message.upper())
print("Count = ",message.count("World"))
print("Index = ",message.find("World"))

new_message = message.replace("World", "Earth")
print(new_message)

#formatting
message = f'{message}, {new_message}'
print(message)
#to get help on class on function
#help(str)
