""" PROJECT PSIT 2018 """
"""หมายเหตุ V.2 นำดีบัคของ V.1 ออกและ ***น่าจะ*** เป็นโค้ดที่สมบูรณ์ที่สุด"""
import csv
import pygal #หมายเหตุ ต้องติดตั้งโปรแกรมเพิ่มเติมถึงจะรัน imprt pygal ได้
def main(set_year, analyze, view_dc, rate_dc):
    """ Sol """
    view_marvel, rate_marvel = dict(), dict()
    print('งานการมี แต่ไม่ทำ')

    find_year('rate_of_dc.csv', set_year)
    find_year('rate_of_marvel.csv', set_year)
    for year in range(min(set_year), max(set_year)+1):#เรียงลำดับปีตั้งแต่ปีแรกจนถึงปีล่าสุดที่มีหนังเข้าโรง
        analyze[str(year)] = None

    view_dc, rate_dc = separate('rate_of_dc.csv', analyze, reset_analyze(analyze))
    view_dc, rate_dc = list(view_dc.values()), list(rate_dc.values())

    view_marvel, rate_marvel = separate('rate_of_marvel.csv', reset_analyze(analyze), reset_analyze(analyze), [])
    view_marvel, rate_marvel = list(view_marvel.values()), list(rate_marvel.values())

    graph(set_year, view_dc, view_marvel, ['Marvel & DC (คนดูในแต่ละปี)', 'view_bar.svg', 'รวมยอดคนดู ตั้งแต่ปี 2005-2018', 'view_pie.svg'])
    graph(set_year, rate_dc, rate_marvel, ['Marvel & DC (เรตติ้งในแต่ละปี)', 'rate_bar.svg', 'รวมเรตติ้งคนดู ตั้งแต่ปี 2005-2018', 'rate_pie.svg'])

def find_year(name_file, set_year):
    """Find a year."""
    """หาปีที่ค่าย DC และ Marvel เข้าปีแรกในจนถึงปัจจุบัน"""
    data = csv.reader(open(name_file))
    for line in data:
        if "date" not in line:
            set_year.add(int(line[1]))
    return set_year

def separate(name_file, analyze, rate):
    """Data analysis and data extraction."""
    check_rate, check_view, data = 0, "", csv.reader(open(name_file))
    for line in data:#ลูปแยก Rate กับ View
        if 'date' not in line:
            check_rate = float(line[2])
        check_view = line[-1]
        while "," in check_view:#เอา "," ออกจากยอด View
            point = check_view.find(",")
            check_view = check_view[:point]+check_view[point+1:]
        if line[1] in analyze:#ปีนั้นมีหนังเข้าโรงหนัง
            if analyze[line[1]] == None:#นำยอด View และ Rate เข้า Dict
                analyze[line[1]] = int(check_view)
                rate[line[1]] = float("%.1f"%check_rate)
            else:#ในกรณีที่ใน1ปีมีมากกว่า 1 เรื่อง
                analyze[line[1]] += int(check_view)
                rate[line[1]] = float("%.1f"%((check_rate+rate[line[1]])/2))#เฉลี่ย Rate
        check_view, check_rate = "", 0
    return analyze, rate

def reset_analyze(analyze):
    """Remain the same value Need to reset."""
    """analyze1 ยังคงมีค่าเก่าที่คิดไปแล้วอยู่จึงต้องทำให้Viewกลับมาเป็น Noneเพื่อเอาไปใช้ต่อ"""
    analyze1 = dict()
    for year in analyze:
        analyze1[year] = None
    return analyze1

def graph(set_year, dc, marvel, name):
    """Create a graph"""
    """สร้างกราฟทั้งแบบ แท่ง และ วงกลม"""
    #set_year = ปี
    #name = ชื่อกราฟ
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
