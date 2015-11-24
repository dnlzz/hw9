# CS288 Homework 9
# Read the skeleton code carefully and try to follow the structure
# You may modify the code but try to stay within the framework.

import libxml2
import sys
import os
import commands
import re
import sys

#import MySQLdb

from xml.dom.minidom import parse, parseString

# for converting dict to xml 
from cStringIO import StringIO
from xml.parsers import expat

def get_elms_for_atr_val(tag,atr,val):
   lst=[]
   elms = dom.getElementsByTagName(tag)
   # ............
   for e in elms:
      if e.nodeType == 1:
         lst.append(e)
   return lst

# get all text recursively to the bottom
def get_text(e):
   lst=[]   
   # ............
   if e.nodeType in (3, 4):
      lst.append(e.nodeValue)
   else:
      for x in e.childNodes:
         lst = lst + get_text(x)
   return lst

# replace whitespace chars
def replace_white_space(str):
   p = re.compile(r'\s+')
   new = p.sub(' ',str)   # a lot of \n\t\t\t\t\t\t
   return new.strip()

# replace but these chars including ':'
def replace_non_alpha_numeric(s):
   p = re.compile(r'[^a-zA-Z0-9:-]+')
   #   p = re.compile(r'\W+') # replace whitespace chars
   new = p.sub(' ',s)
   return new.strip()

# convert to xhtml
# use: java -jar tagsoup-1.2.jar --files html_file
def html_to_xml(fn):
   # ............
   xhtml_file = os.system('java -jar tagsoup-1.2.1.jar --files ' + fn)   
   return xhtml_file

def extract_values(dm):
   lst = []
   #l = get_elms_for_atr_val('tr','class','most_actives')
   # ............
   #need to make list 100 elements here with filter...

   l_trs = dom.getElementsByTagName('tr')
   filtered = filter(lambda x: len(x.childNodes)==6, l_trs)
   del filtered[0]
   print len(filtered)
   
   l_txts = map(lambda x: get_text(x), filtered)
   print len(l_txts)

   for e in l_txts:
      print e

   # ............
   return lst

def tr_to_dict(x):
   d={}
   lst=x[1].split(' (')
   d['name']=lst[0]
   d['symbol']=lst[1]
   d['volume']=lst[2]
   d['price']=lst[3]
   d['change']=lst[4]
   d['percent_change']=lst[5]
   
   return d

# mysql> describe most_active;
def insert_to_db(l,tbl):
   # ............

   # show databases;
   # show tables;
   return 0
   
def main():
   html_fn = sys.argv[1]
   fn = html_fn.replace('.html','')
   #fn = html_fn.replace('.xhtml','')
   #xhtml_fn = html_to_xml(html_fn)
   xml = html_to_xml(html_fn)
   xhtml_fn = fn + ".xhtml"
   global dom
   dom = parse(xhtml_fn)
   
   lst = extract_values(dom)
   
   """
   # make sure your mysql server is up and running
   cursor = insert_to_db(lst,fn) # fn = table name for mysql

   l = select_from_db(cursor,fn) # display the table on the screen

   # make sure the Apache web server is up and running
   # write a PHP script to display the table(s) on your browser
   """
   return xml
# end of main()

if __name__ == "__main__":
    main()

# end of hw7.py
