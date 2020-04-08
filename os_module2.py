import os
from datetime import datetime
# print(dir(os)) #all the functions
# print(os.getcwd())
# os.chdir('/Users/ROHIT/Desktop/python/Python')
# print(os.listdir())
os.removedirs('os-Demo/test')
os.makedirs('os-Demo/test')
# os.rmdir('os-Demo')
print(os.stat('file.py'))
print(os.stat('file.py').st_mtime)
print(datetime.fromtimestamp(os.stat('file.py').st_mtime))

for path, dir1, file in os.walk(os.getcwd()):
    print(path)
    print(dir1)
    print(file)
    print()

# print(os.environ.get('path').split(';')[1]+'/test.txt')
print(os.path.join(os.getcwd(), 'test1.txt'))

print(os.path.isdir(os.getcwd()))
print(os.path.isfile(os.getcwd()))

