""" PROJECT PSIT 2018 """
import csv
def function():
    """ Something """
    print('Let Do IT')
    #DC
    file = open('rate_of_dc.csv')
    data = csv.reader(file)
    table_dc = []
    table_view_dc = dict()
    check_view_dc = ""
    for i in data:
        table_dc += [[*(i[:2]), i[-1]]]
        for j in i[-1]:
            if j != ",":
                check_view_dc += j
        if i[1] in table_view_dc and i[1] != 'date':
            table_view_dc[i[1]] = (int(check_view_dc)+table_view_dc[i[1]])//2
        elif i[1] not in table_view_dc and i[1] != 'date':
            table_view_dc[i[1]] = int(check_view_dc)
        check_view_dc = ""
    print(*(table_dc), sep="\n")
    print()
    for i in table_view_dc:
        print(i, table_view_dc[i])
    #Marvel
    file = open('rate_of_marvel.csv')
    data = csv.reader(file)
    table_marvel = []
    table_view_marvel = dict()
    check_view_marvel = ""
    for i in data:
        table_marvel += [[*(i[:2]), i[-1]]]
        for j in i[-1]:
            if j != ",":
                check_view_marvel += j
        if i[1] in table_view_marvel and i[1] != 'date':
            table_view_marvel[i[1]] = (int(check_view_marvel)+table_view_marvel[i[1]])//2
        elif i[1] not in table_view_marvel and i[1] != 'date':
            table_view_marvel[i[1]] = int(check_view_marvel)
        check_view_marvel = ""
    print(*(table_marvel), sep="\n")
    print()
    for i in table_view_marvel:
        print(i, table_view_marvel[i])
function()
