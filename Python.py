""" PROJECT PSIT 2018 """
import csv
import pygal
def function(set_check, view):
    """ Sol """
    view_dc = dict()
    view_marvel = dict()
    graph_dc = list()
    graph_marvel = list()
    print('งานการมี แต่ไม่ทำ')
    find_year('rate_of_dc.csv', set_check)
    find_year('rate_of_marvel.csv', set_check)
    for year in range(min(set_check), max(set_check)+1):
        view[str(year)] = "-"
    view_dc = calculate_view('rate_of_dc.csv', view, reset_view(view), [], "DC")
    view_dc = list(view_dc.values())
    view_marvel = calculate_view('rate_of_marvel.csv', reset_view(view), reset_view(view), [], "Marvel")
    view_marvel = list(view_marvel.values())


    for i in view_dc:
        if i == '-':
            graph_dc.append(None)
        else:
            graph_dc.append(int(i))
    for i in view_marvel:
        if i == '-':
            graph_marvel.append(None)
        else:
            graph_marvel.append(int(i))
    #print(graph_dc)
    #print(graph_marvel)


    """ กราฟ แท่ง (คนดู) """
    line_chart = pygal.Bar()
    line_chart.title = 'Marvel & DC (ยอดคนดูในแต่ละปี)'
    line_chart.x_labels = map(str, range(2005, 2019))
    line_chart.add('DC', graph_dc)
    line_chart.add('Marvel', graph_marvel)
    line_chart.render_to_file('ตาราง.svg')

    """ กราฟ วงกลม (คนดู)"""
    pie_chart = pygal.Pie()
    pie_chart.title = 'รวมยอดคนดู ตั้งแต่ปี 2005-2018'
    pie_chart.add('DC', graph_dc)
    pie_chart.add('Marvel', graph_marvel)
    pie_chart.render_to_file('ตาราง1.svg')


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
                view[i[1]] += view[i[1]]
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
    print('Year', ' Total_View')

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



function(set(), dict())
