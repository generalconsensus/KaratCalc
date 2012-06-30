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
  con = mdb.connect('localhost', '', '', '');
  cur = con.cursor()
  Sql="SELECT price,Unix_Timestamp(lastdate),browser,ip from details order by lastdate DESC LIMIT 1"
  cur.execute(Sql)
  rows = cur.fetchall()
  for row in rows:
   #print row[1]
   #print now
   last_upd=row[1]

 except IOError as e:
   last_upd=0

 if now-last_upd>1300:
  
  from xml.dom.minidom import parseString
   
  file = urllib2.urlopen('http://www.xmlcharts.com/cache/precious-metals.xml')
  data = file.read()
  file.close()
  dom = parseString(data)
  for plist in dom.getElementsByTagName('pricelist'):
   a=plist.attributes["currency"]
   if a.value=="usd": 
    for node in plist.getElementsByTagName('price'):
     b=node.attributes["commodity"]
     if b.value=="gold":
      #print node.toxml()
      c=node.toxml()
      xmlData=re.sub ('<price .*">', '', c)
      xmlData=re.sub ('</price>', '', xmlData)
      #print "xmlData is %s\n" %(xmlData)
  
  Sql='INSERT INTO details (price, lastdate, browser, ip) values (%.2f, From_unixtime(%d), "%s","%s")' % (float(xmlData), now, "user-agent", "2.2.2.2")
  cur.execute(Sql)

 else:
  print "no upd"
  xmlData=row[0]

  
 return float(xmlData),row[1]
  
(price,time)=get_price("usd")
print "Curr is %2f and time is %f" %(price, time)
