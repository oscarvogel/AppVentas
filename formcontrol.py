#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  formcontrol.py
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

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from login.logincodes import LoginControl
from login.logincodes import AfterLogin

class FormControl(AnchorLayout):
    '''
    classdocs
    '''

    def __init__(self, **kwargs):
        '''
        Constructor
        '''
        super(FormControl,self).__init__(**kwargs)
        c= LoginControl()
        c.setparent(self)
        self.add_widget(c)

    def changewidget(self,to):
        if to == 'AfterLogin':
            self.clear_widgets()
            self.add_widget(AfterLogin())
