#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.9.0')

from kivy.app import App
from formcontrol import FormControl

class MyApp(App):

    def build(self):
        self.title="App Ventas"
        self.formcontrol = FormControl()
        return self.formcontrol

if __name__ == '__main__':
    MyApp().run()
