# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 07:52:22 2021

@author: 13m0nD3m0n
"""

from tkinter import*
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Encapsulation")
root.geometry("800x600")

class Juice:
    def __init__(self, fruit_name, quantity):
        self.fruit = fruit__name
        self.quantity = int(quantity)
        self.__cost = 250
        
    def __caculateCost(self):
        total_cost = self.quantity * self.__cost
        print("You have to pay : "+str(total_cost)+" USD")
        if(self.fruit == "Apple"):
            calorie = self.quantity * 52
        elif(self.fruit == "Mango"):
            calorite = self.quantity * 60
        elif(self.fruit == "Orange"):
            calorie = self.quantity * 47
        print("x"+str(self.quantity)+ " = "+str(calorie)+" calories")
        
    def getCost(self):
        self.__caculateCost()
        
def orderJuice():
    fruit = "Orange"
    quantity = 200
    obj1 = Juice(fruit,quantity)
    obj1.getCost()
    
btn = Button(root, text="TOTAL", command = orderJuice)
btn.place(relx=0.95,rely = 0.5, anchor= E)
root.mainloop()