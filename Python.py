""" PROJECT PSIT 2018 """
import csv
def function():
    """ Something """
    print('Let Do IT')
    file = open('rate_of_dc.csv')
    data = csv.reader(file)
    set_check = set()
    view = dict()
    for year in data:
        if "date" not in year:
            set_check.add(int(year[1]))
    file = open('rate_of_marvel.csv')
    data = csv.reader(file)
    for year in data:
        if "date" not in year:
            set_check.add(int(year[1]))
    for year in range(min(set_check), max(set_check)+1):
        view[str(year)] = "-"
    calculate_view('rate_of_dc.csv', view, [])
    view1 = dict()
    for i in view:
        view1[i] = "-"
    calculate_rate('rate_of_dc.csv', view1, [])
    for i in view1:
        view[i] = "-"
    calculate_view('rate_of_marvel.csv', view, [])
    for i in view:
        view1[i] = "-"
    calculate_rate('rate_of_dc.csv', view1, [])

def calculate_view(name, view, table):
    print('view')
    file = open(name)
    data = csv.reader(file)
    check_view = ""
    for i in data:
        if 'date' not in i:
            table += [[*(i[:2]), i[-1]]]
        for num in i[-1]:
            if num != ",":
                check_view += num
        if i[1] != 'date' and i[1] in view:
            if view[i[1]] != "-":
                view[i[1]] = (int(check_view)+view[i[1]])//2
            else:
                view[i[1]] = int(check_view)
        check_view = ""
    print(*(table), sep="\n")#Output
    print()
    for i in view:#Output
        print(i, view[i])

def calculate_rate(name, view, table):
    print('rate')
    file = open(name)
    data = csv.reader(file)
    check_view = 0
    for i in data:
        if i[2] != 'rate':
            check_view = float(i[2])
        if i[1] != 'date' and i[1] in view:
            if view[i[1]] != "-":
                view[i[1]] = (check_view+view[i[1]])//2
            else:
                view[i[1]] = check_view
        check_view = 0
    for i in view:#Output
        print(i, view[i])

function()
