f = open('test.txt', 'r+')
print(f.name)
print(f.mode)
f.close()

#using context manager, no need to colose
with open('test.txt', 'r+') as f:
    # f_context = f.read()
    # print(f_context)

    # f_context = f.readlines()
    # print(f_context)

    # f_context = f.readline()
    # print(f_context, end='')

    # f_context = f.readline()
    # print(f_context, end='')

    # for line in f:
    #     print(line, end='')

    # f_context = f.read(10)
    # print(f_context)

    # size_to_read = 10
    # f_context = f.read(size_to_read)

    # while len(f_context) > 0:
    #     print(f_context, end='')
    #     f_context = f.read(size_to_read)

    with open('testWrite.txt', 'w') as fw:
        fw.write('5) 5th Line\n')
        fw.write('6) 6th Line\n')
        fw.write(f.read())

with open('eye.jpg', 'rb') as rf:
    with open('eye_copy.jpg', 'wb') as wf:
        chunk = rf.read(1024)
        while len(chunk) > 0:
            wf.write(chunk)
            chunk = rf.read(1024)
