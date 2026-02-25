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

# Monthly expense Tracker
import pandas as pd
dict={
    "Categories":["Food","Transport","Food","Entertainment","Transport","Food"],
    "Amounts":[120,50,200,300,40,100],
    "Days":[1,1,5,10,12,20]
}
columns=["Categories","Amounts","Days"]
df=pd.DataFrame(dict,columns=columns)
print(df)
print("\n")
print("Only amounts are:")
print(df["Amounts"])
print("\n")
print("Only categories are:")
print(df["Categories"])
df["GST"]=df["Amounts"]*0.10
print("After adding gst column:")
print(df["GST"])
print("Total amount")
print(df["Amounts"].sum())
print("\n")
print("Maximum expense is:")
print(df.loc[df["Amounts"].idxmax()])
print("\n")
print("Minimum expenses:")
print(df.loc[df["Amounts"].idxmin()])


# Student marks per subject
import pandas as pd
dict={
    "Name":["Sushmita","Samruddhi","Sharanya","Nishmitha"],
    "Maths":[90,99,87,56],
    "Physics":[56,76,45,33],
    "Chemistry":[34,21,67,85],
    "Attendence":[75,98,65,78]
}
columns=["Name","Maths","Physics","Chemistry","Attendence"]
df=pd.DataFrame(dict,columns=columns)
print(df)
df["Total Marks"]=df["Maths"]+df["Physics"]+df["Chemistry"]
print("After adding total marks column:")
print(df["Total Marks"])
df["Average"]=df["Total Marks"]/3
print("After adding average:")
print(df["Average"])
def grade(avg):
    if avg >= 80:
        return "A"
    elif avg >=60:
        return "B"
    elif avg >=40:
        return "C"
    else:
        return "Fail"
    
df["Grade"]=df["Average"].apply(grade)
print("The grades are:")
print(df["Grade"]


# online order analysis
import pandas as pd
data={
    "Order_ID":[1237,876,453,234,342],
    "Customer":["Ranjita","Sharadvi","Sanika","Tanu","Shobha"],
    "Product":["Mobile","Dress","Laptop","Earphones","Washing Machine"],
    "Quantity":[2,3,1,2,1],
    "Price":[23000,1200,55000,3000,15000]
}
columns=["Order_ID","Customer","Product","Quantity","Price"]
df=pd.DataFrame(data,columns=columns)
print(df)
df["Total price"]=df["Quantity"]*df["Price"]
print("The total prices are:")
print(df["Total price"])
print("The person who spent most is:")
print(df.loc[df["Total price"].idxmax()])

# Cricket Math Statistics
import pandas as pd
data={
    "Player":["Dhoni","virat","Raina","Jadeja","Ruturaj"],
    "Runs":[23,45,56,78,99],
    "Balls":[15,23,20,35,85],
    "Fours":[1,2,5,5,2],
    "Sixes":[1,2,1,4,2]
}
columns=["Player","Runs","Balls","Fours","Sixes"]
df=pd.DataFrame(data,columns=columns)
print(df)
df["Strike Rate"]=(df["Runs"]/df["Balls"])*100
print("The strike rate is:")
print(df["Strike Rate"])
print("Highest score:")
print(df.loc[df["Runs"].idxmax()])
print("Best strike rate:")
print(df.loc[df["Strike Rate"].idxmax()])
print("Players scored more than 50:")
print(df["Runs"]>50)
df["Total boundaries"]=df["Fours"]+df["Sixes"]
print("Players who hit more than 5 boundaries:")
print(df[df["Total boundaries"]>5])

# Hospital Patient data
import pandas as pd
data={
    "Patient name":["Kashyap","Sushmita","Koustubh","Kalyan"],
    "Age":[21,19,20,22],
    "Gender":["Male","Female","Male","Male"],
    "Disease":["Thypoid","Maleriya","Fever","Ring worm"],
    "Bill_amount":[25000,34000,20000,56000]
}
columns=["Patient name","Age","Gender","Disease","Bill_amount"]
df=pd.DataFrame(data,columns=columns)
print(df)
print("Average bill amount is:")
df["Average"]=df["Bill_amount"].mean()
print(df["Average"])
print("Highest bill disease:")
print(df.loc[df["Bill_amount"].idxmax()])
print("Patient above age 50:")
print(df[df["Age"]>50])
print("Total patients per disease:")
print(df.groupby("Disease").size())
print("Average bill per disease:")
print(df.groupby("Disease")["Bill_amount"].mean())
avg_bill=df["Bill_amount"].mean()
print("Bills above average:")
print(df[df["Bill_amount"]>avg_bill])
