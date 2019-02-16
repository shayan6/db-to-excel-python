import time, datetime
import pymysql as db
import pandas as pd
import numpy as np
import warnings
import sys
import csv
warnings.filterwarnings("ignore")



def import_custom(query_custom, h, u, p, d):
 try:
     con = db.connect(host = h, user = u, password = p, db = d)
     with con:
         df = pd.read_sql_query(query_custom, con)
 except Exception as e:
     print("DB ERROR: " + str(e))
 return df

try:
     df = import_custom("SELECT * FROM " + sys.argv[1], h='localhost', u='root', p='', d='tez_mis')
except  Exception:
     output = 'Invalid Table Name'

df.to_csv( r"D:\inetpub\wwwroot\tez\view\php\downloads\ " + sys.argv[1] + ".csv" , index = False )

print('success')
