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




