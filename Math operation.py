# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:16:37 2020

@author: Padiga
"""

annualIncome = 100000.00
bonus = 20.00

tax = 2.5

year = 12

monthlyIncome = ((annualIncome / year) + bonus) - tax


print(monthlyIncome)