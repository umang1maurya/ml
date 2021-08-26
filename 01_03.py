#matplotlib tutorials.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def first(): #introduction
    #line plot
    x=[2,3,4,5]
    y=[4,1,6,2]

    #initialize plot
    plt.plot(x,y)
    plt.title("line graph")
    plt.ylabel("y")
    plt.xlabel("X")
    #plt.show()

    #this will print only star
    plt.plot(x,y,"*")
    plt.title("line graph")
    plt.ylabel("y")
    plt.xlabel("X")
    #we can use line on this 
    plt.plot(x,y)
    #plt.show()

    z=np.arange(0,3*np.pi,0.1)
    zz=np.sin(z)
    plt.plot(z,zz)
    #plt.show()

    #use of scatter graph
    plt.scatter(z,zz)
    plt.show()

    #comparision of graph
    plt.scatter(zz,z,color="g",linewidths=5)
    plt.scatter(z,zz,color="r",linewidth=7)

    #we can use anotation
    plt.annotate(xy=[2,3],s="First line")
    plt.annotate(xy=[4,4],s="second line")

    #we can also use corner details section
    plt.legend(['first line','second line'],loc=4)
    plt.show()



def second(): #bar graph
    #vertical bar graph only bar function
    x=[2,3,4,5]
    y=[4,1,6,2]

    #for vertical bar graph
    plt.bar(x,y)
    #for horizontal bar graph
    plt.barh(x,y)
    plt.title("line graph")
    plt.ylabel("y")
    plt.xlabel("X")
    plt.show()

def third(): #bubble graph and pie chart
    x=[2,3,4,5,32] #required at least five points
    y=[4,1,6,2,23]

    #for bubble graph
    plt.scatter(x,y,s=(np.random.rand(5))*1000,c=np.random.rand(5))
    plt.title("line graph")
    plt.ylabel("y")
    plt.xlabel("X")
    plt.show()

    #for pie chart
    z=[1,2,3,4,1,43,23]
    #for labels 
    label=['a','b','c','d','e','f','g']
    #we can explode it 
    explode=(0,0,1.1,0,1,1,2)


    plt.pie(z,labels=label,explode=explode,shadow=True)
    plt.show()






third()