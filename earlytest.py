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

SPACING = 10


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

        toDoArray = []
        toDoArray.append((QCheckBox(), QLabel("Write a Python program")))
        toDoArray.append((QCheckBox(), QLabel("Go to Trader Joe's")))
        toDoArray.append((QCheckBox(), QLabel("Eat a BURRITO")))




#        grid.addWidget(title, 1, 0)
        buttonAdd = QPushButton("Add")
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(buttonAdd, 1, 0 )

        for i in range (0,len(toDoArray)):
            if i > SPACING - 2:
                continue
            box, task = toDoArray[i]
            grid.addWidget(box, i+2, 0)
            grid.addWidget(task, i+2, 1)


#         buttonCheck = QCheckBox();
#         grid.addWidget(QCheckBox(), 2, 0)
#         grid.addWidget(authorEdit, 2, 1)

#         grid.addWidget(review, 3, 0)
# #        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Review')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())