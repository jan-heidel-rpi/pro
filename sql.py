import sqlite3
import sys
import os
if os.path.exists('pierre.db'):
    print('hallo')
    sys.exit(0)
connection =sqlite3.connect('pierre.db')
cursor = connection.cursor()
