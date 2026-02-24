# Mobile rate
import pandas as pd

data = [
    ["iPhone", 5, 70000],
    ["Samsung", 8, 55000],
    ["Redmi", 10, 15000],
    ["Realme", 6, 18000]
]

columns = ["Brand", "Units_Sold", "Price"]
df = pd.DataFrame(data, columns=columns)
print(df)
print("\n")
print("Price column")
print(df["Price"])
print("\n")
print("Samsung row:")
print(df[df["Brand"]=="Samsung"])
print("\n")
# print("Units sold for redmi:")
# print(df[df["Brand"]=="Redmi"]["Units_sold"])
df["Revenue"]=df["Units_Sold"]*df["Price"]
print("After adding Revenue column:")
print(df)
print("\n")
print("Total revenue:")
print(df["Revenue"].sum())
print("\n")
print("Most expensive phone:")
print(df.loc[df["Price"].idxmax()])
print("\n")
print("Cheapest phone:")
print(df.loc[df["Price"].idxmin()])
print("\n")
print("Type of df:",type(df))
print("Type of df['Revenue']:",type(df["Revenue"]))

# daily small expenses
import pandas as pd
data={
    "Item":["Tea","Bus","Snacks","Book"],
    "Amount":[20,50,30,150]
}
columns=["Item","Amount"]
df=pd.DataFrame(data, columns=columns)
print(df)
print("\n")
print("Amount column")
print(df["Amount"])


