# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 19:18:09 2021

@author: Agamdeep S. Chopra
Title: HW_3
Class: BIA 660, Spring 2021
"""

import requests
from bs4 import BeautifulSoup  
import pandas as pd
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

#Q1
def getReviews(page_url):    
    cols = ['reviewer','source','content','date','score']
    colslice = ["unstyled bold articleLink","subtle critic-publication","the_review","review-date subtle small","small subtle review-link"]
    reviews = None
    target = []
    outcome = []
    soup = BeautifulSoup(requests.get(page_url).content, 'html.parser')
    for j in soup.find_all(class_="row review_table_row"):
        for k in range(len(colslice)):
            i = j.find(class_=colslice[k])
            outcome.append(i.text.strip()) if k!=4 else outcome.append((None if ''.join(e for e in i.text.strip() if e.isalnum())== "FullReview" else '/'.join(ch for ch in i.text.strip() if ch.isdigit())))
    for k in range(int(len(outcome)/5)):
        if outcome[k*5+4] != None:
            if len(outcome[k*5+4])>3:
                outcome[k*5+4] = outcome[k*5+4].replace('/', '.', 1) #Fixing double '/' for reviews whose numerator is not in integer format.
            elif outcome[k*5+4]=='':
                outcome[k*5+4] = None
                print("Warning: Invalid Score Entry Detected (Not a Numeric Score). Assigning None...") # Assigning None value to non numeric scores. I did this because one of the score value was not a numeric score.
        target.append(outcome[(k*5):(k*5+5)])
    reviews = pd.DataFrame(target,columns=cols) 
    return reviews

#Q Bonus
def getReviews_bonus(page_url):    
    cols = ['reviewer','source','content','date','score']
    colslice = ["unstyled bold articleLink","subtle critic-publication","the_review","review-date subtle small","small subtle review-link"]
    reviews = None
    target = []
    outcome = []
    flag = True
    base_url = page_url
    while flag:
        soup = BeautifulSoup(requests.get(page_url).content, 'html.parser')
        for j in soup.find_all(class_="row review_table_row"):
            for k in range(len(colslice)):
                i = j.find(class_=colslice[k])
                outcome.append(i.text.strip()) if k!=4 else outcome.append((None if ''.join(e for e in i.text.strip() if e.isalnum())== "FullReview" else '/'.join(ch for ch in i.text.strip() if ch.isdigit())))
        for k in range(int(len(outcome)/5)):
            if outcome[k*5+4] != None:
                if len(outcome[k*5+4])>3:
                    outcome[k*5+4] = outcome[k*5+4].replace('/', '.', 1)
                elif outcome[k*5+4]=='':
                    outcome[k*5+4] = None
            target.append(outcome[(k*5):(k*5+5)])
        outcome = []
        temp_url = soup.find('a',{"data-qa":"next-btn"})['href']
        if temp_url != '#':
            s = temp_url.index("&")
            page_url = base_url
            page_url += temp_url[s:]
        else: 
            flag= False
        soup.decompose()
        temp_url = None
        s = 0
    reviews = pd.DataFrame(target,columns=cols)
    return reviews

if __name__ == "__main__":  
    
    #url = 'https://www.rottentomatoes.com/m/soul_2020/reviews?type=top_critics'
    url = 'https://www.rottentomatoes.com/m/coco_2017/reviews?type=top_critics'
    
    reviews=getReviews(url)
    print(reviews.head(5))
    
    print("\nbonus-")
    reviews_b=getReviews_bonus(url)
    print(reviews_b.head(90))
    