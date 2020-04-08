import import_module as im
import sys
new_list = ['Math', 'Art', 'Eng']
# index = import_module.find_index(new_list, 'Art')
index = im.find_index(new_list, 'Art')
print("index = ", index)
# print(sys.path)

import random
print(random.choice(new_list))

import math
print(math.radians(90))
print(math.sin(math.radians(90)))

import datetime
import calendar
print(datetime.date.today())
print(calendar.isleap(2020))




