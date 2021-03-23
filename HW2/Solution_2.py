# Homework Assignment 2: Numpy Array and DataFrame
# Agamdeep S. Chopra
# 02/26/2021
# BIA 660, Spring 2021
# Score: 13/10

#%%
# Q1
def analyze_tf(X):
       
    tf_idf = None
   
    # Add your code here
    df = np.count_nonzero(X,axis=0)
    tf = np.divide(X,np.sum(X,axis=0))
    tf_idf = np.divide(tf,df)
    #print index of the longest document
    print("Indexes of the longest documents:",np.argmax(np.sum(X,axis=1)))
    #print indexes of words with the top 3 largest 𝑑𝑓 values
    print("Indexes of words with the top 3 largest df values:",df.argsort()[-3:][::-1])
    #return index of top_3 words in the longest document
    print("Indexes of words with top 3 largest tf_idf values in the longest document:",tf_idf[np.argmax(np.sum(X,axis=1)),:].argsort()[-3:][::-1])
    return tf_idf

#%%
# Q2
def emotion_analysis():
    # add your code
    df = pd.read_csv("emotion.csv")
    count_ems = df["emotion"].value_counts()
    print("\n===The number of samples labeled for each emotion===\n",count_ems)
    df['length'] = df['text'].str.count(' ') + 1
    #print(df['length'])
    print("\n=== min, max, and mean values of sadness, happiness, and text length for each emotion===")
    sumry = df.groupby('emotion').agg({'sadness': ['mean','min', 'max'],'happiness': ['mean', 'min', 'max'],'length': ['mean', 'min', 'max']})
    print(sumry)
    print("\n=== Cross tabulation of anxiety score by emotion and worry ===")
    print(pd.crosstab(df["emotion"], df["worry"],df["anxiety"],aggfunc='mean'))
    
#%%
# Q3
def find_coocur(x):
    c = np.array(x) 
    c = np.dot(c.T,c)
    np.fill_diagonal(c,0)
    return c

#%%
# Structure of your solution to Assignment 1 

import numpy as np
import pandas as pd

# best practice to test your class
# if your script is exported as a module,
# the following part is ignored
# this is equivalent to main() in Java

if __name__ == "__main__":  
    
    # Test Question 1
    print("\n")
    print("=== Test Question 1 ===")
    
    dtm = pd.read_csv("dtm.csv")
    x = dtm.values
    analyze_tf(x)
    
    print("\n")
    print("=== Test Question 2 ===")
    emotion_analysis()
    
    print("\n")
    print("=== Test Question 3 ===")
    print(find_coocur(x))
    