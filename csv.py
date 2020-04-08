import csv
with open('names.csv', 'r') as rf:
    with open('cpy_names.csv', 'w') as wf:
        for line in rf:
            line = line.split(',')
            wf.write('-'.join(line))
            print(line)
        # f.read()
        # print(data)
