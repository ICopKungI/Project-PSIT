""" PROJECT PSIT 2018 """
"""หมายเหตุ V.2 นำดีบัคของ V.1 ออกและ ***น่าจะ*** เป็นโค้ดที่สมบูรณ์ที่สุด"""
import csv
import pygal #หมายเหตุ ต้องติดตั้งโปรแกรมเพิ่มเติมถึงจะรัน imprt pygal ได้
def main(set_check, analyze, view_dc, rate_dc):
    """ Sol """
    view_marvel, rate_marvel = dict(), dict()

    print('งานการมี แต่ไม่ทำ')

    find_year('rate_of_dc.csv', set_check)
    find_year('rate_of_marvel.csv', set_check)
    for year in range(min(set_check), max(set_check)+1):#เรียงลำดับปีตั้งแต่ปีแรกจนถึงปีล่าสุดที่มีหนังเข้าโรง
        analyze[str(year)] = None

    view_dc, rate_dc = separate('rate_of_dc.csv', analyze, reset_analyze(analyze), [], "DC")
    view_dc, rate_dc = list(view_dc.values()), list(rate_dc.values())

    view_marvel, rate_marvel = separate('rate_of_marvel.csv', reset_analyze(analyze), reset_analyze(analyze), [], "Marvel")
    view_marvel, rate_marvel = list(view_marvel.values()), list(rate_marvel.values())

    graph(set_check, view_dc, view_marvel, ['Marvel & DC (คนดูในแต่ละปี)', 'view_bar.svg', 'รวมยอดคนดู ตั้งแต่ปี 2005-2018', 'view_pie.svg'])
    graph(set_check, rate_dc, rate_marvel, ['Marvel & DC (เรตติ้งในแต่ละปี)', 'rate_bar.svg', 'รวมเรตติ้งคนดู ตั้งแต่ปี 2005-2018', 'rate_pie.svg'])

def find_year(name_file, set_check):
    """Find a year."""
    """หาปีที่ค่าย DC และ Marvel เข้าปีแรกในจนถึงปัจจุบัน"""
    file = open(name_file)
    data = csv.reader(file)
    for year in data:
        if "date" not in year:
            set_check.add(int(year[1]))
    return set_check

def reset_analyze(analyze):
    """Remain the same value Need to reset."""
    """analyze1 ยังคงมีค่าเก่าที่คิดไปแล้วอยู่จึงต้องทำให้Viewกลับมาเป็น Noneเพื่อเอาไปใช้ต่อ"""
    analyze1 = dict()
    for i in analyze:
        analyze1[i] = None
    return analyze1

def separate(name_file, analyze, rate, table_view, name):
    """Data analysis and data extraction."""
    file = open(name_file)
    data = csv.reader(file)
    check_rate, check_view, table_rate = 0, "", []
    for i in data:#ลูปแยก Rate กับ View
        if 'date' not in i:
            check_rate = float(i[2])
            table_view += [[*(i[:2]), i[-1]]]
            table_rate += [i[:3]]
        for num in i[-1]:#เอา "," ออกจากยอด View
            if num != ",":
                check_view += num
        if i[1] in analyze:
            if analyze[i[1]] != None:#ในกรณีที่ใน1ปีมีมากกว่า 1 เรื่อง
                analyze[i[1]] += int(check_view)
                rate[i[1]] = float("%.1f"%((check_rate+rate[i[1]])/2))#เฉลี่ย Rate
            else:#นำยอด View และ Rate เข้า Dict
                analyze[i[1]] = int(check_view)
                rate[i[1]] = float("%.1f"%check_rate)
        check_view, check_rate = "", 0

    return analyze, rate

def graph(set_year, dc, marvel, name):
    """Create a graph"""
    """สร้างกราฟทั้งแบบ แท่ง และ วงกลม"""

    """ กราฟ แท่ง (คนดู) """
    line_chart = pygal.Bar()
    line_chart.title = name[0]#หัวข้อกราฟแท่ง
    line_chart.x_labels = map(str, range(min(set_year), max(set_year)+1))
    line_chart.add('DC', dc)
    line_chart.add('Marvel', marvel)
    line_chart.render_to_file(name[1])#ชื่อไฟล์กราฟแท่ง

    """ กราฟ วงกลม (คนดู)"""
    pie_chart = pygal.Pie()
    pie_chart.title = name[2]#หัวข้อกราฟวงกลม
    pie_chart.add('DC', dc)
    pie_chart.add('Marvel', marvel)
    pie_chart.render_to_file(name[3])#ชื่อไฟล์กราฟ วงกลม

    #หมายเหตุ โค้ดนี้ไม่ได้กดรันแล้วกราฟจะแสดงขึ้นมาทันที่แค่เป็นการสร้างไฟล์กราฟขึ้นมา

main(set(), dict(), dict(), dict())
