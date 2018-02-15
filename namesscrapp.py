import pandas as pd
import os
from selenium import webdriver
import time 
from numpy import random
import csv
os.chdir(r'C:\Users\Juan Pablo\Documents\names')
import codecs


df=pd.read_csv("namestorequestJP.csv",encoding = 'latin1')
namedic={} 
nationdic={}
browser = webdriver.Firefox(executable_path=r"C:\Users\Juan Pablo\gecko\geckodriver.exe")
df.shape
mysize=list(df.shape)[0]-1  # size of names 

for NAM in range(0,mysize):
    try:
        time.sleep( int(random.uniform(7,11)))
        url='http://abel.lis.illinois.edu/cgi-bin/ethnea/search.py?Fname='+df.iloc[NAM,0]+'&Lname='+ \
        df.iloc[NAM,1]
        browser.get(url) 
        browser.refresh()
        time.sleep( int(random.uniform(3,6)))
        linkElemI = browser.find_elements_by_css_selector('table tbody tr')   # caracteristicas de la tabla mas grande 
        linkElemII = browser.find_elements_by_css_selector('body p b ')   # caracteristicas de la tabla mas grande 
    
    
    
        for cc in range(1,len(linkElemI)):
            probsdic={}
            data=str1=linkElemI[cc].text.split()   # here i split the data on Ethnicity Prob First Last probF probL
            probsdic['Prob']=float(data[1])
            try:
                    probsdic['probF']=float(data[4])
                    probsdic['probL']=float(data[5])
            except:
                
                try:
                    
                    probsdic['probF']=float(data[5])
                    probsdic['probL']=float(data[6])
                    
                except:
                    
                    try:
                        probsdic['probF']=float(data[6])
                        probsdic['probL']=float(data[7]) 
                        
                    except:
                        
                         try:
                             probsdic['probF']=float(data[7])
                             probsdic['probF']=float(data[8])
                         except:
                             continue 
                
            nationdic[data[0]]=probsdic
            nationdic['Gender']=linkElemII[0].text
    
        namedic[data[2]+" "+data[3]]=nationdic
        nationdic={}
    except:
        time.sleep( int(random.uniform(30,40)))
        continue

    
df=pd.DataFrame.from_dict(namedic, orient='columns', dtype=None).transpose()
writer = pd.ExcelWriter('namesrequest.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()


    