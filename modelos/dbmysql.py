#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dbmysql.py
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

import MySQLdb as mdb

try:
    mycon = mdb.connect('192.168.0.200', 'root', 'fasca', 'clarita');
   
except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    
