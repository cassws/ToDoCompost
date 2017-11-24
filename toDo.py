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
from data import checkFile, writeFile
from garden import Garden
# import checklist items from data.py

SPACING = 20
FILENAME = 'taskList.txt'

class Checklist(QWidget):
    
    def __init__(self, sessionGarden):
        super().__init__()
        self.sessionGarden = sessionGarden
        self.toDoArray = self.loadToDoItems()


        self.initUI()
        
        
    def initUI(self):
        
        title = QLabel('Title')
        titleEdit = QLineEdit()

        grid = QGridLayout(self)
        grid.setSpacing(SPACING)

        # creates an array of ToDoItem objects
        # based on file data


        # new ToDo button + text box
        buttonAdd = QPushButton("Add")
        buttonSave = QPushButton("Save")
        grid.addWidget(buttonAdd, 1, 0 )
        grid.addWidget(buttonSave, 1, 2 )
        grid.addWidget(titleEdit, 1, 1)
        buttonAdd.clicked.connect(lambda: self.addTask(titleEdit))
        buttonSave.clicked.connect(lambda: writeFile(FILENAME, self.toDoArray))

        for i in range (0,len(self.toDoArray)):
            if i > SPACING - 2:
                continue
            box, task = self.toDoArray[i].CheckBox, self.toDoArray[i].Label
            grid.addWidget(box, i+2, 0)
            grid.addWidget(task, i+2, 1)
        self.setLayout(grid) 
        self.setGeometry(300, 100, 600, 600)
        self.setWindowTitle('To Do Compost')    
        self.show()
        
    def loadToDoItems(self):
        # loads a list of tasks (as an array of paremeters) from a .txt file
        # and returns a list of ToDoItem objects with created from these parameters
        rawTaskData = []
        tdItemArray = []
        rawTaskData = checkFile(FILENAME)
        for item in rawTaskData:
            tdItemArray.append(ToDoItem(label = item[0], sessionGarden = self.sessionGarden))
        return tdItemArray

    def addTask(self, editBar):
        barText = editBar.text()
        if barText:
            print('New ToDo task: ' + barText)
            self.toDoArray.append(ToDoItem(label = barText, sessionGarden = self.sessionGarden))
            self.refreshToDos(self.layout())
            editBar.clear()

    def refreshToDos(self, layout):
        box, task = self.toDoArray[-1].CheckBox, self.toDoArray[-1].Label
        layout.addWidget(box, layout.rowCount(), 0)
        layout.addWidget(task, layout.rowCount()-1, 1)


class ToDoItem(QWidget):

    def __init__(self, label, sessionGarden, priority=1, isChecked=False, tags=[]):
        self.priority = priority
        self.tags = tags
        self.CheckBox = QCheckBox()
        self.Label = QLabel(label)
        self.isChecked = isChecked
        self.CheckBox.stateChanged.connect(lambda: self.crossOffTask())
        self.sessionGarden = sessionGarden
    
    def crossOffTask(self):
        self.isChecked = True
        self.CheckBox.deleteLater()
        self.Label.deleteLater()
        print('Checked off ' + self.Label.text())
        self.sessionGarden.addCompost(self.Label.text())

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    app.processEvents()
    mygarden = Garden()
    cl = Checklist(mygarden)
    sys.exit(app.exec_())