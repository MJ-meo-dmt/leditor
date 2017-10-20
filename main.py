#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python imports

# Panda imports
from direct.showbase.ShowBase import ShowBase


class Leditor(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        print("Leditor begins...")
        

leditor = Leditor()
leditor.run()
