import unittest
import csv
import platform
import openpyxl

xlsx_file = 'C:/Users/rasmu/Documents/Python/Week-6/02-2 Working with Files/iris_data.xlsx'
csv_file = 'C:/Users/rasmu/Documents/Python/Week-6/02-2 Working with Files/newCSV.csv'

#class TestStringMethods(unittest.TestCase):
#
 #   def test_upper(self):
  #      self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    wb = openpyxl.load_workbook(xlsx_file)
    sheet = wb.get_sheet_by_name("Fisher's Iris Data")
    columns = ['A', 'B', 'C', 'D', 'E']

    header = []
    for column_name in columns:
        idx = column_name + '1'
        header.append(sheet[idx].value)
    print(header)
    col_values = []
    for column_name in columns:
        col_idx = openpyxl.utils.column_index_from_string(column_name) - 1
        column = []
        for cell in list(sheet.columns)[col_idx][1:]:
            column.append(cell.value)
        col_values.append(column)
    print(col_values)
    
    
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    with open(csv_file, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(header)
        for row in col_values:
            output_writer.writerow(row)