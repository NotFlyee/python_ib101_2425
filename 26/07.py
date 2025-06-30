import sys, xlsxwriter


def export_check(text: str):
    data = list(map(lambda line: tuple(line.split()), text.split('\n')))

    workbook = xlsxwriter.Workbook('res.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    for name, price, number in data:
        worksheet.write_row(row, 0, [name, float(price), int(number), f'=B{row + 1}*C{row + 1}'])
        row += 1
    worksheet.write_row(row, 0, ['Итого', None, None, f'=SUM(D1:D{row})'])

    workbook.close()


export_check(sys.stdin.read().strip())
