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

def basic_info():
    print("".center(50,"="))
    print("Original Dataset".center(50," "))
    print("".center(50,"="))
    print(df)
    print("".center(50,"="))
    print("Basic information regarding the dataset".center(50," "))
    print("".center(50,"="))
    print(df.info())
    rows,cols=df.shape
    print("Number of rows: ",rows)
    print("Number of columns: ",cols)
    print("Datatype of each column".center(50,"*"))
    print(df.dtypes)
    print("".center(50,"="))
    print("Basic Statistics related to expenses".center(50," "))
    print("".center(50,"="))
    print(df.describe())

def handle_missing_values():
    global df
    df=df[df["Date"].notna()]
    df=df[df["Date"].str.strip() != ""]
    object_cols = df.select_dtypes(include=["object", "string"]).columns
    df[object_cols] = df[object_cols].fillna("Unknown")
    df[object_cols] = df[object_cols].apply(lambda cols:cols.str.strip())
    df = df[(df[object_cols] != "").all(axis=1)]
    print("".center(50,"="))
    print("Expenses after handling missing values".center(50," "))
    print("".center(50,"="))
    print(df)

from datetime import datetime
def convert_datatypes():
    global df
    possible_formats=[
        "%Y-%m-%d",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%d/%m/%Y",
        "%d-%b-%Y",
        "%b-%d-%Y",
        "%Y-%b-%d"
    ]
    for indx,dates in df["Date"].items():
        for fmt in possible_formats:
            try:
                date_obj=datetime.strptime(dates,fmt)
                df.at[indx,"Date"]=date_obj.strftime("%Y-%m-%d")
            except(ValueError):
                continue
    df["Date"]=pd.to_datetime(df["Date"],errors="coerce")
    df=df[df["Date"].notna()]
    df["Amount"]=df["Amount"].str.replace("₹","")
    df["Amount"]=df["Amount"].str.replace(",","")
    df["Amount"]=pd.to_numeric(df["Amount"],errors="coerce")
    df=df[df["Amount"].notna()]
    print("".center(50,"="))
    print("Expenses after converting data types".center(50," "))
    print("".center(50,"="))
    print(df)
    
def standardize_text_descriptions():
    df["Category"]=df["Category"].str.title()
    df["Description"]=df["Description"].str.title()
    print("".center(50,"="))
    print("Expenses after standardizing texts".center(50," "))
    print("".center(50,"="))
    print(df)

def handle_duplicates():
    global df
    df.drop_duplicates(inplace=True,subset=["Date","Category","Description"],keep="first")
    print("".center(50,"="))
    print("Expenses after handling duplicates".center(50," "))
    print("".center(50,"="))
    print(df)

def handle_outliers():
    global df
    q1=df["Amount"].quantile(0.25)
    q3=df["Amount"].quantile(0.75)
    iqr=q3-q1
    lowerbound=q1-1.5*iqr
    upperbound=q3+1.5*iqr
    df = df[(df["Amount"] >= lowerbound) & (df["Amount"] <= upperbound)]
    print("".center(50,"="))
    print("Basic Statistics involved in handling outliers".center(50," "))
    print("".center(50,"="))
    print(f"Quartile 1:{q1}")
    print(f"Quartile 3:{q3}")
    print(f"Inter-Quartile-Range:{iqr}")
    print(f"Lowerbound:{lowerbound}")
    print(f"Upperbound:{upperbound}")
    print("".center(50,"="))
    print("Expenses after handling outliers".center(50," "))
    print("".center(50,"="))
    print(df)

def add_columns():
    df["Year"]=df["Date"].dt.year
    df["Month Name"]=df["Date"].dt.month_name()
    df["Day Name"]=df["Date"].dt.day_name()
    print("".center(50,"="))
    print("Expenses after adding columns".center(50," "))
    print("".center(50,"="))
    print(df)

def final():
    print("".center(50,"="))
    print("Basic Statistics of the Final Expenses Dataset".center(50," "))
    print("".center(50,"="))
    print(df.describe())
    print("\n",df.info())

basic_info()
handle_missing_values()
convert_datatypes()
standardize_text_descriptions()
handle_duplicates()
handle_outliers()
add_columns()
final()