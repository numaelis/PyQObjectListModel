#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:34:27 2020

@author(c++): railwaycoder QObjectListModel https://railwaycoder@bitbucket.org/railwaycoder/qobjectlistmodelqmltesting.git
"performing for qml listmodel"

<<traslate to python3 PySide2: Numael Garay>>
"""
from testobject import TestObject
from qobjectlistmodel import QObjectListModel

import sys

from PySide2.QtCore import Property, QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    
    myObjectListModel = QObjectListModel(app)
    for i in range(200):
        testObject = TestObject(myObjectListModel)
        name = "TestObject "+str(i)
        testObject.setName(name)
        testObject.setColor("red")
        myObjectListModel.append(testObject)
    
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("ObjectListModel", myObjectListModel)
    engine.load(QUrl.fromLocalFile('main.qml'))
    if not engine.rootObjects():
        
        sys.exit(-1)
    sys.exit(app.exec_())
