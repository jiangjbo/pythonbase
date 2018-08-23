# -*- coding: utf-8 -*-

import xlrd

from datetime import date,datetime

excelFile = xlrd.open_workbook(r'E:\\1.xls',encoding_override="cp1252")
names = excelFile.sheet_names()
for name in names:
    sheet = excelFile.sheet_by_name(name)
    columns = sheet.ncols


    rows = sheet.nrows
    rowFirst = sheet.row_values(0)





