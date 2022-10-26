import pandas as pd

df = pd.read_excel('Academic Details.xlsx') #reads the first sheet of your excel file
choice=input("Enter the filtering choice fail / pass")
if choice=="pass":
    df = df[(df['Status']=='pass')] #Filtering dataframe
    print(df)
elif choice=='fail':
    f = df[(df['Status']=='fail')] #Filtering dataframe
    print(f)
else:
    print("Enter correct choice")