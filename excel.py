import xlwt
import xlrd
from datetime import datetime
import os
from xlutils.copy import copy

#file = 'test.xls'
#设置表格样式
def set_style(name,height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

def cj(file):
    if os.path.exists(file):
        f = xlwt.Workbook()
        sheet1 = f.add_sheet('红包细表', cell_overwrite_ok=True)
        sheet2 = f.add_sheet('红包总表', cell_overwrite_ok=True)
        row1 = ["时间", "收入"]
        for i in range(0,len(row1)):
            sheet1.write(0,i,row1[i],set_style('Times New Roman',220,True))
        row2 = ["日期", "收入"]
        for i in range(0,len(row2)):
            sheet2.write(0,i,row2[i],set_style('Times New Roman',220,True))
        f.save(file)
    else:
        pass

def get_jrze(file):
    jrze = 0
    wb = xlrd.open_workbook(filename=file)
    sheet1 = wb.sheet_by_name('红包细表')
    timecols = sheet1.col_values(0)
    for i in range(0,len(timecols)):
        t = timecols[i].split()[0]
        if t in datetime.now().strftime('%Y-%m-%d'):
            jrze = jrze + float(sheet1.col_values(1)[i])
    return jrze

def set_xb_data(file,mon):
    rb = xlrd.open_workbook(file, formatting_info=True)
    wb = copy(rb)
    ws = wb.get_sheet(0)
    sheet2 = rb.sheet_by_name('红包总表')
    cmax = len(sheet2.col_values(0))
    print(cmax)
    ws.write(cmax,0, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    ws.write(cmax,1, mon)
    wb.save(file)

def set_zb_data(file):
    rb = xlrd.open_workbook(file, formatting_info=True)
    wb = copy(rb)
    ws = wb.get_sheet(1)
    sheet1 = rb.sheet_by_name('红包总表')
    cmax = len(sheet1.col_values(0))
    print(cmax)
    ws.write(cmax, 0, datetime.now().strftime('%Y-%m-%d'))
    ws.write(cmax, 1, get_jrze(file))
    wb.save(file)

# for i in range(1,100):
#     set_xb_data(file)
#set_zb_data(file)
