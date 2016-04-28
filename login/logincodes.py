#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  logincodes.py
#  
#  Copyright 2016 Jose Oscar Vogel <oscarvogel@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from kivy.uix.gridlayout import GridLayout


class LoginControl(GridLayout):
    _parentwidget=None

    def __init__(self, **kwargs):
        super(LoginControl,self).__init__(**kwargs)
        self.userid.text=''

    def setparent(self,parent):
        self._parentwidget=parent

    def changewidget(self,to):
        self._parentwidget.changewidget(to)

    def login_pressed(self,button):
        print(button.text)
        print(self.userid.text)
        print(self.userpw.text)
        self.changewidget('AfterLogin')

    def close_pressed(self,button):
        print(button.text)
        exit()


class AfterLogin(GridLayout):

    def __init__(self,**kwargs):
        super(AfterLogin,self).__init__(**kwargs)
