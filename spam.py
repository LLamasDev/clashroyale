#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
from clashroyale import *

db = pymysql.connect('SERVER', 'USER', 'PASSWORD', 'DATA BASE')
cursor = db.cursor()

grupo()

try:
   cursor.execute('UPDATE clanes SET spam = "si"')
   db.commit()
   cursor.execute('UPDATE usuario SET usoHoy = "0"')
   db.commit()
except:
   db.rollback()

db.close()