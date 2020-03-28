if 3 > 2:
    print("Condition is True")
language = "python"

if language == "python":
    print("Condition True")

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = 0

if condition:
    print('Evaluated to True')
elif condition == 0:
    print("elif pass")
else:
    print('Evaluated to False')

val = 2
if condition == 0 and val == 2:
    print("both condition true")


a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a == b)
print(a is b)

a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a == b)
print(a is b)
