import numpy as np
import pandas as pd

#pandas tutorials.

def first(): #pandas tutorials.
    print("\nfirst..........")
    data = {
        'roll_no':[3,1,2,4],
        'paper_id':[34,10,21,11],
        'marks':[32,21,54,23]
    }

    df1=pd.DataFrame(data)
    print(df1)

    #we can change idex also
    df2 = pd.DataFrame(data,index=["a","b","c","d"])
    print(df2)

    #extracting data from index
    print(df2.loc['c'])

    print(df2.iloc[:,-1])

    print(df2.iloc[0:2,2:3])


    print("  ")

def second(): #working on csv data
    data=pd.read_csv("a.csv")
    print(data.head()) #print some head data
    print(data.head(10)) #print 10 datas

    print(data.info()) #print data details

    print(data.describe()) #print data description.

    print(data['label_name'][:5]) #print data only five of lebel

    print(data[['label_name']][:5]) #print details also

    #print multiple label data
    print(data[['label_name','label_name']].head())

    print(data.iloc[:10,1:3]) #print columnn 1 ,2 data upto 3

def third(): #missing values
    data = {
        'roll_no':[3,1,2,4],
        'paper_id':[34,10,21,11],
        'marks':[np.nan,21,54,23]
    }

    df=pd.DataFrame(data)
    print(df)

    #how to check null value in dataframe
    print(df.isnull())
 
    #for checking total null value
    print(df.isnull().sum())

    #fill null value
    df1=df.fillna(21)
    print(df1)

    #dropping null value
    a= df.dropna()
    print(a)

    #dropping a row
    b= df.dropna(axis=0)
    print(b)

    #dropping a column
    c=df.dropna(axis=1)
    print(c)

    #Creating a data with non NULL values
    d=pd.notnull(df["marks"])
    print(d)

    print(df[d])


def fourth():   #statics
    data = {
        'roll_no':[3,1,2,4],
        'paper_id':[34,10,21,11],
        'marks':[32,21,54,23]
    }
    df=pd.DataFrame(data)

    print(df['marks'].sum()) #print sum of marks
    print(df['marks'].mean())
    print(df['marks'].cumsum())
    print(df['marks'].count())
    print(df['marks'].var())
    print(df['marks'].std())
    print(df.corr())


fourth()
