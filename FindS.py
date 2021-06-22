# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 11:41:58 2021

@author: JASON
"""

import csv
a=[]
with open('enjoysprt.csv','r') as csvfile:
    for row in csv.reader(csvfile):
        a.append(row)
    print(a)
print("Total number of hypotheses:",len(a))
num_attr=len(a[0])-1
hypotheses=['0']*num_attr
print("Initital hypotheses:")
print(hypotheses)
for i in range(0,len(a)):
    if a[i][num_attr]=='yes':
        for j in range(0,num_attr):
            if hypotheses[j]=='0' or hypotheses[j]==a[i][j]:
                hypotheses[j]=a[i][j]
            else:
               hypotheses[j]='?'
print("The instance ",format(i+1)," is:\n",hypotheses)
print("The maximally specific hypotheses is:\n",hypotheses)
            