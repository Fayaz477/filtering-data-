import pandas as pd

df = pd.read_excel('Academic Details.xlsx',sheetname=0) #reads the first sheet of your excel file
#for entering the filtering option
choice=input("Enter the filtering choice fail / pass")
#for checking the student status 
if choice=="pass":
    df = df[(df['Status']=='pass')] #Filtering dataframe
    print(df)
elif choice=='fail':
    f = df[(df['Status']=='fail')] #Filtering dataframe
    print(f)
else:
    print("Enter correct choice")
