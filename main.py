"""from turtle import Turtle
from random import random

t = Turtle()
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)
   

t.screen.mainloop()
"""
from prettytable import PrettyTable
table = PrettyTable()


table.field_names=['City name','Area','Population','Annual Rainfall']
table.add_row(["Varanasi",1235,111558,640.65])
table.add_row(["Pune",1285,111558,80.65])
table.add_row(["Mumbai",3242,111558,700.65])
table.add_row(["Gorakhpur",9235,111558,600.65])
print(table)