import xlsxwriter, sys

data = list(map(lambda line: line.split(), sys.stdin.readlines()))

workbook = xlsxwriter.Workbook('res.xlsx')
worksheet = workbook.add_worksheet()

for row, (name, value) in enumerate(data):
    worksheet.write(row, 0, name)
    worksheet.write(row, 1, int(value))

chart = workbook.add_chart({'type': 'pie'})
chart.add_series({'categories': f'=Sheet1!A1:A{len(data)}', 'values': f'=Sheet1!B1:B{len(data)}'})
worksheet.insert_chart('C3', chart)

workbook.close()
