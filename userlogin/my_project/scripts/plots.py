# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:34:17 2019

@author: DIPANSHU VERMA
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

raw = pd.read_excel('Instant Raw Report (11).xlsx')
complains = pd.read_excel('Street light Complaint Details last 6 Month.xlsx')
regr=linear_model.LinearRegression()


complains_unhandled= complains[complains['Call Status']=='OPEN']

s=list(set(complains['District']))
ratio_den={}
ratio_num={}
ratio={}

for item in s:
    ratio_num[item]=len(complains_unhandled[complains_unhandled['District']==item])
    ratio_den[item]=len(complains[complains['District']==item])
    ratio[item]=ratio_num[item]/ratio_den[item]

complains_open=[]
for i in range(len(ratio_num)):
    complains_open.append((list(ratio_num.values())[i],list(ratio_num.keys())[i]))

complains_open.sort()

plt.plot(ratio_num.keys(),ratio_num.values())
plt.xticks(rotation=90)
plt.savefig('D:\open vs cities2')
plt.show()

time=[]
dev_ON=raw[raw['Active Power kW']!=0]
temp=list(dev_ON['Timestamp'])
for i in range(len(dev_ON)):
    z=temp[i].split()[1].split(':')
    time.append(3600*int(z[0])+60*int(z[1])+int(z[2]))

plt.scatter(time,dev_ON['Active Power kW'])    
plt.savefig('D:\working time')

languages_spoken=list(set(complains['Language Preference']))
language={}
for item in languages_spoken:
    language[item]=len(complains[complains['Language Preference']==item])
plt.scatter(language.keys(),language.values())
plt.xticks(rotation=90)
plt.savefig('D:\languages')






