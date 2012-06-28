#!/usr/bin/python
def get_price (curr):
 price=0
 import urllib2
 import re
 import os
 import time
 import MySQLdb as mdb

 now=time.time()

 try:
  con = mdb.connect('localhost', 'jmat_goldview', 'k5o63RAGQ6cbimUgtLmc', 'jmat_gold_history');
  cur = con.cursor()
  Sql="SELECT price,Unix_Timestamp(lastdate),browser,ip from details order by lastdate DESC LIMIT 1"
  cur.execute(Sql)
  rows = cur.fetchall()
  for row in rows:
   #print row[1]
   #print now
   xmlData=row[0]
   last_upd=row[1]

 except IOError as e:
   xmlData=0
   last_upd=0


  
 return float(xmlData),row[1]
  
(price,time)=get_price("usd")
#print "Curr is %2f and time is %f" %(price, time)
