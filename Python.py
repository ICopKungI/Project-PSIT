""" PROJECT PSIT 2018 """
import csv
import pygal
def function(set_check, view):
    """ Sol """
    view_dc, rate_dc = dict(), dict()
    view_marvel, rate_marvel = dict(), dict()

    print('งานการมี แต่ไม่ทำ')

    find_year('rate_of_dc.csv', set_check)
    find_year('rate_of_marvel.csv', set_check)
    for year in range(min(set_check), max(set_check)+1):
        view[str(year)] = "-"
    view_dc, rate_dc = calculate_view('rate_of_dc.csv', view, reset_view(view), [], "DC")
    view_dc1 = none(list(view_dc.values()), [])
    rate_dc1 = none(list(rate_dc.values()), [])

    view_marvel, rate_marvel = calculate_view('rate_of_marvel.csv', reset_view(view), reset_view(view), [], "Marvel")
    view_marvel1 = none(list(view_marvel.values()), [])
    rate_marvel1 = none(list(rate_marvel.values()), [])

    print(view_dc1)
    print(view_marvel1)
    print(rate_dc1)
    print(rate_marvel1)

    """ กราฟ แท่ง (คนดู) """
    line_chart = pygal.Bar()
    line_chart.title = 'Marvel & DC (ยอดคนดูในแต่ละปี)'
    line_chart.x_labels = map(str, range(2005, 2019))
    line_chart.add('DC', view_dc1)
    line_chart.add('Marvel', view_marvel1)
    line_chart.render_to_file('view.svg')

    """ กราฟ วงกลม (คนดู)"""
    pie_chart = pygal.Pie()
    pie_chart.title = 'รวมยอดคนดู ตั้งแต่ปี 2005-2018'
    pie_chart.add('DC', view_dc1)
    pie_chart.add('Marvel', view_marvel1)
    pie_chart.render_to_file('view_all.svg')

    """ กราฟ แท่ง (เรต) """
    line_chart = pygal.Bar()
    line_chart.title = 'Marvel & DC (เรตติ้งในแต่ละปี)'
    line_chart.x_labels = map(str, range(2005, 2019))
    line_chart.add('DC', rate_dc1)
    line_chart.add('Marvel', rate_marvel1)
    line_chart.render_to_file('rate.svg')

    """ กราฟ วงกลม (เรต)"""
    pie_chart = pygal.Pie()
    pie_chart.title = 'รวมยอดคนดู ตั้งแต่ปี 2005-2018'
    pie_chart.add('DC', rate_dc1)
    pie_chart.add('Marvel', rate_marvel1)
    pie_chart.render_to_file('rate_all.svg')

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
                view[i[1]] += int(check_view)
                rate[i[1]] = float("%.1f"%((check_rate+rate[i[1]])/2))
            else:
                view[i[1]] = int(check_view)
                rate[i[1]] = float("%.1f"%check_rate)
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
    return view, rate

def none(lis, graph):
    for i in lis:
        if i == '-':
            graph.append(None)
        else:
            graph.append(i)
    return graph

function(set(), dict())
