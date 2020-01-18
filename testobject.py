#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 22:32:21 2020

@author(c++): railwaycoder QObjectListModel https://railwaycoder@bitbucket.org/railwaycoder/qobjectlistmodelqmltesting.git
"performing for qml listmodel"

<<traslate to python3 PySide2: Numael Garay>>
"""

from PySide2.QtCore import QObject, Signal, Slot, Property

class TestObject(QObject):
    def __init__(self, parent = None):
        QObject.__init__(self, parent)
        self.m_name=""
        self.m_color=""
    
    def _name(self):
        return self.m_name
    def _color(self):
        return self.m_color
    def setName(self, name):
        if name!= self.m_name:
            self.m_name=name
            self.nameChanged.emit()
    def setColor(self, color):
        if color!= self.m_color:
            self.m_color=color
            self.colorChanged.emit()
    @Signal
    def nameChanged(self):
        pass
    
    @Signal
    def colorChanged(self):
        pass    
    name = Property(str, _name, setName, notify= nameChanged)
    color = Property(str, _color, setColor, notify= colorChanged)
