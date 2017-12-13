#!/usr/bin/python3
# -*- coding:utf-8 -*-  

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import time

# print( time.time() )
# print( time.strftime("%Y-%m-%d %H:%M:%S") )
# import datetime
# print( datetime.datetime.now() )
# print( datetime.datetime.now().strftime('%Y-%m-%d %H:%M') )

exit()

resp = urlopen("https://www.asdbi.com/").read().decode("utf-8")

soup = bs(resp,"html.parser")

res = soup.findAll("tr", {"class": "tbtrcoinboard_1"})

# print(res)

for item in res:
	logo = item.find("img")['src']
	name = item.find("td").get_text().lstrip()
	price = item.select("td:nth-of-type(2)")[0].get_text().replace("￥","")
	diff = item.select("td:nth-of-type(3)")[0].get_text()
	tradeNum = item.select("td:nth-of-type(4)")[0].get_text()
	tradePrice = item.select("td:nth-of-type(5)")[0].get_text().replace("￥","")
	time = time.time();
	date = time.strftime("%Y-%m-%d %H:%M:%S")
	# print( name.encode('utf-8').decode('utf-8') )
	# print( "{logo:%s,name:%s,price:%s,diff:%s,tradeNum:%s,tradePrice:%s}\n" %(logo,name,price,diff,tradeNum,tradePrice) )
	
	fo = open("foo.md", "a")
	fo.write( "{logo:%s,name:%s,price:%s,diff:%s,tradeNum:%s,tradePrice:%s}\n" %(logo,name.encode('unicode-escape'),price,diff,tradeNum,tradePrice) )
	fo.close()
	# print(item)
	break

