expenses = [
    {"Date": "2025-01-02", "Category": "Food", "Amount": "250", "Description": "Lunch"},
    {"Date": "02/01/2025", "Category": "food ", "Amount": "₹300", "Description": "Dinner"},
    {"Date": "2025-1-3", "Category": "Transport", "Amount": 120, "Description": "Bus ticket"},
    {"Date": "03-Jan-2025", "Category": "TRANSPORT", "Amount": "120.0", "Description": "Bus Ticket"},
    {"Date": "2025/01/04", "Category": "Entertainment", "Amount": "500 ", "Description": "Movie"},
    {"Date": "", "Category": "Groceries", "Amount": "850", "Description": "Vegetables"},
    {"Date": "2025-01-05", "Category": None, "Amount": "600", "Description": "Milk and bread"},
    {"Date": "2025-01-06", "Category": "Utilities", "Amount": "", "Description": "Electricity bill"},
    {"Date": "2025-01-07", "Category": "Food", "Amount": "-150", "Description": "Refund"},
    {"Date": "2025-01-08", "Category": "Shopping", "Amount": "1,200", "Description": "Clothes"},
    {"Date": "2025-01-09", "Category": "shopping", "Amount": "1200", "Description": "clothes"},
    {"Date": "2025-13-10", "Category": "Travel", "Amount": "2500", "Description": "Train ticket"},
    {"Date": "2025-01-11", "Category": "Travel ", "Amount": "2500.50", "Description": "train Ticket"},
    {"Date": "11-01-2025", "Category": "travel", "Amount": "2500.5", "Description": "Train ticket"},
    {"Date": "2025-01-12", "Category": "Health", "Amount": "five hundred", "Description": "Medicines"},
    {"Date": "2025-01-13", "Category": "Health", "Amount": None, "Description": "Doctor visit"},
    {"Date": "2025-01-14", "Category": "Bills", "Amount": "750", "Description": "Internet"},
    {"Date": "2025-01-14", "Category": "Bills", "Amount": "750", "Description": "Internet"},
    {"Date": "2025-01-15", "Category": "Food", "Amount": "300", "Description": None},
    {"Date": "2025-01-16", "Category": "Education", "Amount": "1500", "Description": "Books"},
    {"Date": "2025-01-16", "Category": "Education", "Amount": "1500", "Description": "books"},
    {"Date": "2025-01-17", "Category": "Entertainment", "Amount": "999999999", "Description": "Game"},
    {"Date": "2025-01-18", "Category": "Food", "Amount": "0", "Description": "Unknown"},
    {"Date": "2025-01-19", "Category": "Food", "Amount": " 450 ", "Description": "Snacks"},
    {"Date": "2025-01-20", "Category": "Groceries", "Amount": "850.00", "Description": "vegetables"},
    {"Date": "2025-01-20", "Category": "Groceries", "Amount": "850", "Description": "Vegetables"}
]

import pandas as pd
df=pd.DataFrame(expenses)
print("".center(50,"="))
print("Entire dataframe")
print(df)
print(df.head()) #prints first 5 rows of the dataframe
print(df.tail()) #prints last 5 rows of the dataframe
print(df.info())#prints number of rows ,number of columns ,datatype of each column,missing values
print(df.shape)#prints number of rows and columns
rows,cols=df.shape
print("Number of rows: ",rows)
print("Number of columns: ",cols)
print(df.dtypes)#prints datatype of each column
#df["Date"]=pd.to_datetime(df["Date"])
print(df.dtypes)
#print(df.describe())gives statistical summary of numerical columns
#summary = df.describe()
#summary.loc["mean", "Amount"]gives mean of the amount column
#summary.loc["50%", "Amount"]gives median of amount column
#summary.loc["25%", "Amount"]gives q1 of amount column
#summary.loc["75%", "Amount"]gives q3 of amount column
#summary.loc["max", "Amount"]gives maximum value of amount column
#summary.loc["min","Amount"]gives minimum value of amount column
#summary.loc["std","Amount"]gives standard deviation of amount column
#alternative method to do the same
#df["Amount"].count()
#df["Amount"].mean()
#df["Amount"].std()
#df["Amount"].min()
#df["Amount"].quantile(0.25)   # Q1
#df["Amount"].median()         # Q2
#df["Amount"].quantile(0.75)   # Q3
#df["Amount"].max()
#print(df.isna())tells whether the each value is present or not , False->present True->Missing value
#print(df.isna().sum())counts total missing values in each column
#print(df.fillna(0))fills every missing value with 0
#fills each column differently
#df["Name"] = df["Name"].fillna("Unknown")
#df["Age"] = df["Age"].fillna(0)
#df["City"] = df["City"].fillna("Not Specified")
#print(df.dropna())removes rows containing missing values
#print(df.dropna(axis=1))removes columns containing missing values
#print(df.dropna(how="all"))removes the row only if all values in the row are missing
#print(df.dropna(subset=["Age"]))removes row only if a specific column is missing
#df["Amount"] = df["Amount"].astype(int)#converts the data type of amount column to int
#df["Amount"] = pd.to_numeric(df["Amount"])#safer as it can also handle invalid values and converts into float
#df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")#this logic takes care of invalid values
#converts data types of multiple columns at once
#df = df.astype({
#    "Amount": float,
 #   "Category": str
#})
#more robust as it can handle invalid values by stating Nan there
#df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
#df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
print(df.describe(include="all"))#gives statistical summary of all columns
print("".center(50,"="))

print("".center(50,"="))
print("Column related functions")
print(df.columns) #gives a list of columns in the dataframe 'df'
print("Prints only date column".center(50,"*"))
print(df["Date"])
print(type(df["Date"])) #shows that each value corresponding to the key in a column is stored in series form
print(df[["Category","Amount"]])#inorder to access more than one columns
col=df.columns
print(df[col])
print("".center(50,"="))

print("".center(50,"="))
print("Row related functions")
print(df.iloc[0])#prints first row of the dataframe
print(df.iloc[1:7])#iloc-->works with integer locations
print(type(df.iloc[0]))#shows each row is stored in the form of series
print(df.loc[:5,"Category":"Description"])#loc-->works with labels
print("".center(50,"="))

