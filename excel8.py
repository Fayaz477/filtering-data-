
from openpyxl import Workbook
wb = Workbook()
sheet = wb.active

#For changing column name 
sheet['A1'] = "StudentName"
sheet['B1'] = "Mark"
sheet['C1'] = "Status"
limits=int(input("Enter the limits"))

#for entering the values in excel
for i in range(1,limits):
    sheet["A"+str(i+1)]= input("Enter the student name:")
    sheet["B"+str(i+1)]= input("Enter the mark:")
    sheet["C"+str(i+1)]= input("Enter the status of student:")

#for saving the file
wb.save('Academic Details.xlsx')





