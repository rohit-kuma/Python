print("Module Imported")
def find_index(newList, target):
    for index, value in enumerate(newList):
        # print(index, value, target)
        if value == target:
            # print("found = ", index, value, target)
            return index
    return -1
