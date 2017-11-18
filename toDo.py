#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Modified from ZetCode PyQt5 tutorial 

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
    QTextEdit, QCheckBox, QPushButton, QGridLayout, QApplication)
from data import checkFile

# import checklist items from data.py

SPACING = 10
FILENAME = 'taskList.txt'

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(SPACING)

        # creates an array of ToDoItem objects
        # based on file data
        toDoArray = self.loadToDoItems()

#        grid.addWidget(title, 1, 0)
        buttonAdd = QPushButton("Add")
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(buttonAdd, 1, 0 )

        for i in range (0,len(toDoArray)):
            if i > SPACING - 2:
                continue
            box, task = toDoArray[i].CheckBox, toDoArray[i].Label
            grid.addWidget(box, i+2, 0)
            grid.addWidget(task, i+2, 1)

        
        self.setLayout(grid) 
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Review')    
        self.show()
        
    def loadToDoItems(self):
        # loads a list of tasks (as an array of paremeters) from a .txt file
        # and returns a list of ToDoItem objects with created from these parameters
        rawTaskData = []
        tdItemArray = []
        rawTaskData = checkFile(FILENAME)
        for item in rawTaskData:
            tdItemArray.append(ToDoItem(item[0]))
        return tdItemArray

class ToDoItem(QWidget):

    def __init__(self, label, priority=1, isChecked=False, tags=[]):
        self.priority = priority
        self.tags = tags
        self.CheckBox = QCheckBox()
        self.Label = QLabel(label)
        self.isChecked = isChecked
    
    def crossOffTask(self):
        self.isChecked = True
        # do special things when task is checked off!

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())