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
def initial():
    print("".center(50,"="))
    print("Number of initial records: ",len(expenses))
    print("".center(50,"="))

def handle_missing_values():
    global expenses
    cleaned=[expense for expense in expenses if 
             expense["Date"] is not None and 
             expense["Date"].strip() != ""]
    for expense in cleaned:
        if expense["Category"] == None:
            expense["Category"] = "Miscellaneous"
        if expense["Amount"] == None or str(expense["Amount"]).strip() == "":
            expense["Amount"]=0.0
        if expense["Description"] == None:
            expense["Description"] = "Unknown"
    print("".center(50,"="))
    print("Expenses after handling missing values".center(50," "))
    print("".center(50,"="))
    expenses=cleaned
    print("{:<15}{:<15}{:<15}{}".format(
    "Date", "Category", "Amount", "Description"))
    for expense in expenses:
        print("{:<15}{:<15}{:<15}{}".format(
            expense["Date"],
            expense["Category"],
            expense["Amount"],
            expense["Description"]))
        
def remove_leading_trailing_spaces():
    for expense in expenses:
        for i in expense:
            if not isinstance(expense[i],str):
                expense[i]=str(expense[i])
            expense[i]=expense[i].strip()
    print("".center(50,"="))
    print("Expenses after removing leading and trailing spaces".center(50,"="))
    print("".center(50,"="))
    print(f"{"Date":<15}{"Category":<15}{"Amount":<15}Description")
    for expense in expenses:
        print(f"{expense["Date"]:<15}"
              f"{expense["Category"]:<15}"
              f"{expense["Amount"]:<15}"
              f"{expense["Description"]}")

def convert_datatypes():
    print("="*50)
    print("Expenses after handling different types of formats of amounts")
    print("="*50)
    for expense in expenses:
        if isinstance(expense["Amount"],str):
            try:
                expense["Amount"]=expense["Amount"].replace("₹","")
                expense["Amount"]=expense["Amount"].replace(",","")
                expense["Amount"]=float(expense["Amount"])
                if expense["Amount"] < 0.0:
                    expense["Amount"]=0.0
            except(ValueError,TypeError):
                expense["Amount"]=0.0
    print("{:<15}{:<15}{:<15}{}".format("Date","Category","Amount","Description"))
    for expense in expenses:
        print("{:<15}{:<15}{:<15}{}".format(
            expense["Date"],
            expense["Category"],
            expense["Amount"],
            expense["Description"]
        ))

from datetime import datetime
def standardise_dates():
    global expenses
    print("="*50)
    print("Expenses after handling different formats of dates")
    print("="*50)
    cleaned=[]
    possible_formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%d-%b-%Y",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%Y-%b-%d"
    ]
    for expense in expenses:
        for fmt in possible_formats:
            try:
                date_obj=datetime.strptime(expense["Date"],fmt)
                expense["Date"]=date_obj.strftime("%Y-%m-%d")
                cleaned.append(expense)
            except(ValueError):
                continue
    expenses=cleaned
    print("{:<15}{:<15}{:<15}{}".format("Date","Category","Amount","Description"))
    for expense in expenses:
        print("{:<15}{:<15}{:<15}{}".format(
            expense["Date"],
            expense["Category"],
            expense["Amount"],
            expense["Description"]
        ))

def standardize_text_desccriptions():
    for expense in expenses:
        for i in expense:
            if isinstance(expense[i],str):
                expense[i]=expense[i].title()
    print("".center(50,"="))
    print("Expenses after standardizing texts")
    print("".center(50,"="))
    print("{:<15}{:<15}{:<15}{}".format("Date","Cateogory","Amount","Description"))
    for expense in expenses:
        print("{:<15}{:<15}{:<15}{}".format(
            expense["Date"],
            expense["Category"],
            expense["Amount"],
            expense["Description"]
        ))

def handle_duplicates():
    global expenses
    cleaned=[]
    f=0
    for expense in expenses:
        for i in cleaned:
            f=0
            if (expense["Date"] == i["Date"] and 
            expense["Category"] == i["Category"] and
            expense["Amount"] == i["Amount"] and
            expense["Description"] == i["Description"]) :
                f=1
        if f == 0:
            cleaned.append(expense)
    expenses=cleaned
    print("".center(50,"="))
    print("Data after handling duplicates")
    print("".center(50,"="))
    print("{:<15}{:<15}{:<15}{}".format("Date","Category","Amount","Description"))
    for expense in expenses:
        print("{:<15}{:<15}{:<15}{}".format(
            expense["Date"],
            expense["Category"],
            expense["Amount"],
            expense["Description"]
        ))

def handle_outliers():
    global expenses
    print("".center(50,"="))
    print("Statistics behind identifying outliers\n\n")
    date=[int(expense["Amount"]) for expense in expenses]
    date=sorted(date)
    print("Sorted Amount Column: ",date)
    if len(date) % 2 == 0:
        q2= date[((len(date))//2+((len(date))+1)//2)//2]
    else:
        q2=date[(len(date))//2]
    print("Median Value for the Amount column: ",q2)
    less_than=[]
    greater_than=[]
    for d in date:
        if d < q2:
            less_than.append(d)
        elif d > q2:
            greater_than.append(d)
    print("list of amounts for q1: ",less_than)
    print("list of amounts for q2: ",greater_than)
    q1=less_than[(len(less_than))//2]
    q3=greater_than[(len(greater_than)+1)//2]
    print("Quartile1: ",q1)
    print("Quartile3: ",q3)
    iqr=q3-q1
    print("Inter-Quartile-Range: ",iqr)
    lowerbound=q1-1.5*iqr
    upperbound=q3+1.5*iqr
    print("Lowerbound: ",lowerbound)
    print("Upperbound: ",upperbound)
    print("".center(50,"="))
    cleaned=[]
    for expense in expenses:
        if int(expense["Amount"]) > lowerbound and int(expense["Amount"]) < upperbound:
            cleaned.append(expense)
    expenses=cleaned
    print("".center(50,"="))
    print("Expenses after handling outliers")
    print("".center(50,"="))
    print("{:<15}{:<15}{:<15}{}".format("Date","Category","Amount","Description"))
    for expense in expenses:
        print("{:<15}{:<15}{:<15}{}".format(
            expense["Date"],
            expense["Category"],
            expense["Amount"],
            expense["Description"]
        ))

def add_columns():
    for expense in expenses:
        date_obj=datetime.strptime(expense["Date"],"%Y-%m-%d")
        expense["Year"]=date_obj.year
        expense["Month"]=date_obj.month
        expense["Day"]=date_obj.strftime("%A")
    print("".center(50,"="))
    print("Expenses after Year Month and Day columns")
    print("".center(50,"="))
    print("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{}".format("Date","Year","Month","Day","Category","Amount",
                                                          "Description"))
    for expense in expenses:
        print("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{}".format(
            expense["Date"],
            expense["Year"],
            expense["Month"],
            expense["Day"],
            expense["Category"],
            expense["Amount"],
            expense["Description"]))

def final():
    print("".center(50,"="))
    print("Number of final records: ",len(expenses))
    print("".center(50,"="))
            


initial()
handle_missing_values()
remove_leading_trailing_spaces()
convert_datatypes()
standardise_dates()
standardize_text_desccriptions()
handle_duplicates()
handle_outliers()
add_columns()
final()