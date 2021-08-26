import numpy as np
#num py tutorials

def first():      ######1.1 use of numpy 
    print("\nfirst methods .........")
    #Creating a numpy arr.
    list1=[1,2,4,5,6,7,7] #this is normal list.
    list2=np.array(list1) #this is numpy array.

    print(list2)    #print numpy array
    print(type(list2))  #print type of numpy array

    #we can add a number to all
    print(list2+2)

    #we can create 2d list like this.

    #we can convert list to float
    list3=np.array(list2,dtype='float')
    print(list3)

    #we can convert list3 to int and other data_type.
    list4=list3.astype(int)
    print(list4)

    print(" ")


def second():   #######1.2 array dimensions 
    print("\nSecond  ...................")
    arr4 = np.array([[4,5,23,12.0],['a','b',43,43]],dtype=object)
    print("Shape of array : " ,arr4.shape )
    print("Size of array : ",arr4.size)
    print("Type of array  : ",arr4.dtype)
    print("Dimensions : ",arr4.ndim)

    print(" ")


def third():    #reversing rows and columns.
    print("\n Third ....................")
    arr4 = np.array([[4,5,23,12.0],['a','b',43,43]],dtype=object)
    arr6=np.array([1,2,3,4,5,6])
    print(arr6)
    print(arr6[::-1]) #this reverse the array
    print("normal 2d array : ",arr4)
    print("[::-1] reverse only row ",arr4[::-1]) #reverse the 2d array
    print("[::-1,::-1] reverse column ",arr4[::-1,::-1]) #this will reverse as well as columns

    print(" ")

def fourth(): #specific element extraction
    print("\n Fourth..........")
    arr4 = np.array([[4,5,23,12.0],['a','b',43,43]],dtype=object)
    arr6=np.array([1,2,3,4,5,6])
    print(arr4[0,:]) #give only the first array data
    print(arr4[:1,:]) #give only the first element
    print(arr4[:2,:]) #give the two  array list col,row

    print(" ")

def fifth(): #Basic statics
    print("\n Fifth..........")
    arr6=np.array([1,2,3,4,5,6])
    print(arr6.mean()) #gives the mean of array. 
    print("sum of array : ",arr6.sum()) #gives the sum of array element.
    print("max of array : ",arr6.max()) #give the max of array element.
    print("min of array : ",arr6.min()) #gives the min of array element.
    print("Median of array : ",np.median(arr6)) 
    print("average of array : ",np.average(arr6))
    print("variance of array : ",np.var(arr6)) 
    print(" ")

def sixth(): #Reshaping and flattening.
    print("\n sixth..........")
    arr6=np.array([1,2,3,4,5,6])
    arr4 = np.array([[4,5,23,12.0],['a','b',43,43]],dtype=object)
    print("shape of array : ",arr4.shape)
    print("reshape of array : ",arr4.reshape(4,2)) #it must of dimension of product equal to product of arry dimension

    print("Change it to single dimension : ",arr4.flatten())
    print("dimension of array ", arr4.ndim)

    print(" ")


def seventh(): #Creating random array and sequences.
    print("\n seventh..........")
    arr1=np.arange(10) #this will create an array size 10 and initialize value 0,1,2...9
    print(arr1)
    print("create array of 2 to 8 ",np.arange(2,8)) # 2 3 4 5 6 7
    print("create array with step size ",np.arange(2,10,3)) #2 5 8
    #np.arange(10,0) gives error
    print("create reverse array ",np.arange(10,0,-1)) #10 9 ..1

    print("Create an array with auto calculate ",np.linspace(10,20,4))
    print("Create array with zero value ",np.zeros([2,3])) #for 3d [2,3,4]

    print(" ")


def eigth(): #Unique items and count.
    print("\n eigth..........")
    arr=np.array([[1,2,3,4,5,4,2],[3,4,90,12,321,21,23]])
    val,count=np.unique(arr,return_counts=True)

    print("Unique value : ",val)
    print("Freqency     : ",count)
    

    print(" ")

eigth()