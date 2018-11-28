""" PROJECT PSIT 2018 """
import csv
def function(set_check, view):
    """ Sol """
    print('Let Do IT')
    find_year('rate_of_dc.csv', set_check)
    find_year('rate_of_marvel.csv', set_check)
    for year in range(min(set_check), max(set_check)+1):
        view[str(year)] = "-"
    calculate_view('rate_of_dc.csv', view, reset_view(view), [], "DC")
    calculate_view('rate_of_marvel.csv', reset_view(view), reset_view(view), [], "Marvel")

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
    check_rate, calculate_view, table_rate = 0, "", []
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
    print()
    print('Table view', name)
    print(*(table_view), sep="\n")#Output
    print('View', name)
    for i in view:#Output
        print(i, view[i])
    print('Table rate', name)
    print(*(table_rate), sep="\n")#Output
    print('Rate', name)
    for i in rate:#Output
        if rate[i] != "-":
            print(i, "%.1f"%(rate[i]))
        else:
            print(i, rate[i])

function(set(), dict())
