import xlsxwriter

workbook = xlsxwriter.Workbook(r'd:\text1.xlsx')
worksheet = workbook.add_worksheet()

for num in range(1, 11):
    row = "A"+str(num)
    # worksheet.write_row(row, str(num))
    worksheet.write_string(0,1,"hey")

workbook.close()