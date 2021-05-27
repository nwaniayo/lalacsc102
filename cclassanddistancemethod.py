# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:13:51 2021

@author: SST-LAB
"""

class Xbank:
    def __init__(self,theatmpin,theaccountbalance,thename):
        self.atmpin=theatmpin
        self.accountbalance=theaccountbalance
        self.name=thename
        
    def CollectMoney(self ,amounttowithdraw):
        if (amounttowithdraw > self.accountbalnce):
            print("Sorry we are not able toprocess this at this time")
        else:
            print("Collect your cash.... Thanks for banking with Xbank")
            
    def ChangePins(self, newPin):
        self.atmpin=newPin
        print("Your Pin has been changed ...Thanks for banking with Xbank")
        
    def ChangePin(self, newPin):
        self.atmpin=newPin
        print(f"Your pin has been changed ...Thanks for banking with Xbank")
    @classmethod()
   def NoOfcustomersLoggedin(cls):
       print("we have a total of" + str(Xbank.loggedincounter) + "that have logged in")
       
f=open(" )