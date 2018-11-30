""" PROJECT PSIT 2018 """
import csv
import pygal
def function(set_check, view):
    """ Sol """
    view_dc = dict()
    view_marvel = dict()
    print('งานการมี แต่ไม่ทำ')
    find_year('rate_of_dc.csv', set_check)
    find_year('rate_of_marvel.csv', set_check)
    for year in range(min(set_check), max(set_check)+1):
        view[str(year)] = "-"
    view_dc = calculate_view('rate_of_dc.csv', view, reset_view(view), [], "DC")
    view_marvel = calculate_view('rate_of_marvel.csv', reset_view(view), reset_view(view), [], "Marvel")


    print(view_dc)
    print(view_marvel)

def find_year(name_file, set_check):
    """Find a year."""
    file = open(name_file)
    data = csv.reader(file)
    for year in data:
        if "date" not in year:
            set_check.add(int(year[1]))
    return set_check

def reset_view(view):
    """Remain the same value Need to reset."""
    view1 = dict()
    for i in view:
        view1[i] = "-"
    return view1

def calculate_view(name_file, view, rate, table_view, name):
    """Data analysis and data extraction."""
    file = open(name_file)
    data = csv.reader(file)
    check_rate, check_view, table_rate = 0, "", []
    for i in data:
        if 'date' not in i:
            check_rate = float(i[2])
            table_view += [[*(i[:2]), i[-1]]]
            table_rate += [i[:3]]
        for num in i[-1]:
            if num != ",":
                check_view += num
        if i[1] in view:
            if view[i[1]] != "-":
                view[i[1]] = (int(check_view)+view[i[1]])//2
                rate[i[1]] = (check_rate+rate[i[1]])/2
            else:
                view[i[1]] = int(check_view)
                rate[i[1]] = check_rate
        check_view, check_rate = "", 0

    """ สั่ง Print ตาราง """

    print()
    print('Table view', name) #ยอดคนรวม
    print()
    print("['Movie_Name', 'Year', 'View']")
    print(*(table_view), sep="\n")#Output
    print()
    print('View', name)#เฉลี่ยคนดู
    print()
    print('Year', ' Average_View')

    for i in view:#Output
        print(i, view[i])
    print()
    print('Table rate', name)#rateรวม
    print()
    print("['Movie_Name', 'Year', 'Rate']")
    print(*(table_rate), sep="\n")#Output
    print()
    print('Rate', name)#เฉลี่ยrate
    print()
    print('Year', ' Average_Rate')

    for i in rate:#Output
        if rate[i] != "-":
            print(i, "%.1f"%(rate[i]))
        else:
            print(i, rate[i])
    return view


    """ กราฟ """
    line_chart = pygal.Bar()
    line_chart.title = 'Marvel & DC [View]'
    line_chart.x_labels = map(str, range(2005, 2019))
    line_chart.add('Marvel', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('DC',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.render_to_file('ตาราง.svg')

function(set(), dict())
