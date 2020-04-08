import os
print(os.getcwd())
# print(os.__file__)

os.chdir('/Users/ROHIT/Documents/test')
print(os.getcwd())

list1 = os.listdir()
print(list1)
for f in list1:
    # print(f)
    print(f[:f.find('.jpg')])

for f in os.listdir():
    # print(os.path.splitext(f)[0])
    # print(os.path.splitext(f)[1])
    file, ext  = os.path.splitext(f)
    title, num = file.split(' ')
    num = num.split('_')[1].zfill(2)
    # title = title.strip() #strips the whitespace if any
    # print(num, title, ext)
    #below shows why to use formated string
    new_name = f'{num}-{title}{ext}'
    # print(new_name)
    os.rename(f, new_name)
    # print(ext)
    print(os.listdir())

