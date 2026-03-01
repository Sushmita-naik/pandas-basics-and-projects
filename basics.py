# # Series
import pandas as pd
a=pd.Series([1,2])
print(a)
var=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'],dtype="float",name="python") # to change the data type
print(var)
print(type(var))
print(var[2]) # to find the index


import pandas as pd
dic= {  # using dictionaries
    "name":['python','c','c++','java',],
    "popularity":[90,85,87,34],
    "rank":[1,2,5,10]
}
var=pd.Series(dic)
print(var)

import pandas as pd
var=pd.Series(20,index=['a','b','c','d','e'])
var2=pd.Series(20,index=['a','b','c'])
print(var+var2)
print(var)
print(type(var))

# dataframes in pandas
# in list
import pandas as pd
list=[1,2,3,4,5]
var=pd.DataFrame(list)
print(var)
print(type(var))

# in dictionary
dict={
    "a":[1,2,3,4,5],
    "b":[5,6,7,8,9],
    "d":[12,13,14,24,65],
    1:[12,3,4,5,6]
    
}
# var2=pd.DataFrame(dict,columns=["a",1],index=["a","b","c","d","e"]) # to print only one column elements here a,b is column and values are rows elements
var2=pd.DataFrame(dict)
print(var2)
print(type(var2))
print(var2["a"][3])

# using list under list
list_1=[[1,2,3,4,5],[45,6,7,8,22]]
var4=pd.DataFrame(list_1,index=["a","b"])
print(var4)
print(type(var4))

# using series
series={
    "s":pd.Series([1,2,3,4]),
    "t":pd.Series([2,3,4,5])
}
var=pd.DataFrame(series)
print(var)

# dataframe delete and insert function
# insert function
import pandas as pd
var=pd.DataFrame({"a":[1,2,3,4,5],"B":[4,5,6,7,9]})
print(var)
var.insert(2,"C++",var["a"])
print(var)
var.insert(3,"Sush",var["B"])
print(var)
var.insert(0,"An",[10,11,12,13,14])
print(var)
var["Sushmita"]=var["a"][:3]
print(var)

# delete function
import pandas as pd
var=pd.DataFrame({"a":[1,2,3,4,5],"B":[4,5,6,7,9],"C":[11,12,13,14,15]})
print(var)
var1=var.pop("C")
print(var1)
del var["a"]
print(var)


# CSV file
import pandas as pd
dict={1:[1,2,3,4,5,6],2:[1,2,3,4,5,6],3:[1,2,3,4,5,6]}
d=pd.DataFrame(dict)
print(d)
d.to_csv("Test_new1.csv",index=False,header=[1,2,3])

# read csv file
import pandas as pd
csv_file1=pd.read_csv("C:\\Users\\sushm\\OneDrive\\Desktop\\Pandas\\customers-100.csv")
print(csv_file1)

# to get the rows
csv_file1=pd.read_csv("C:\\Users\\sushm\\OneDrive\\Desktop\\Pandas\\Sale Report.csv",nrows=6)
print(csv_file1)
print(type(csv_file1))

# to get the colums 
csv_file1=pd.read_csv("C:\\Users\\sushm\\OneDrive\\Desktop\\Pandas\\Sale Report.csv",usecols=["SKU Code","Design No.","Category"])
print(csv_file1)

# to get the column using method2 
csv_file1=pd.read_csv("C:\\Users\\sushm\\OneDrive\\Desktop\\Pandas\\Sale Report.csv",usecols=[0,1,2])
print(csv_file1)

# to skip the rows
csv_file1=pd.read_csv("C:\\Users\\sushm\\OneDrive\\Desktop\\Pandas\\Sale Report.csv",skiprows=[0,1,2,3,4,5])
print(csv_file1)

# to change the index 
csv_file1=pd.read_csv("C:\\Users\\sushm\\OneDrive\\Desktop\\Pandas\\Sale Report.csv",index_col="SKU Code")
print(csv_file1)

# To change the header 
csv_file1=pd.read_csv("C:\\Users\\sushm\\OneDrive\\Desktop\\Pandas\\Sale Report.csv",header=2)
print(csv_file1)

# to change the header method2
csv_file1=pd.read_csv("C:\\Users\\sushm\\OneDrive\\Desktop\\Pandas\\Sale Report.csv",names=["colm1","colm2","com3","colm4,colm5,colm6,colm7"])
print(csv_file1)

# to change the header method3
csv_file1=pd.read_csv("C:\\Users\\sushm\\OneDrive\\Desktop\\Pandas\\Sale Report.csv",header=None)
csv_file1.columns=["Colm1","Colm2","Colm3","Colm4","Colm5","Colm6","Colm7"]
print(csv_file1)

# to change the datatype of datas
import pandas as pd
csv_file1=pd.read_csv("C:\\Users\\sushm\\OneDrive\\Desktop\\Pandas\\Sale Report.csv",dtype={"Colm4":int})
print(csv_file1)
