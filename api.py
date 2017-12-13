from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from time import strftime,time
from db import Db

class Api(object):

	def __init__(self):
		pass
		
	def getContent(self, url):
		resp = urlopen(url).read().decode("utf-8")
		soup = bs(resp,"html.parser")
		return soup

	# 什币网 https://www.asdbi.com
	def asdbi(self):
		soup = self.getContent("https://www.asdbi.com/")
		res = soup.findAll("tr", {"class": "tbtrcoinboard_1"})

		#list 保存所有结果到
		tepList = []
		for item in res:
			# dict记录信息
			temp = {
				'logo': 'https://www.asdbi.com' + item.find("img")['src'], 
				'name': item.find("td").get_text().lstrip(), 
				'price': item.select("td:nth-of-type(2)")[0].get_text().replace("￥",""),
				'diff':item.select("td:nth-of-type(3)")[0].get_text().replace("%",""),
				'tradeNum':item.select("td:nth-of-type(4)")[0].get_text(),
				'tradePrice':item.select("td:nth-of-type(5)")[0].get_text().replace("￥",""),
				'from':'www.asdbi.com',
				'upTime':time(),
				'upDate':strftime("%Y-%m-%d %H:%M:%S")
			}

			tepList.append( temp )
			sqls = "insert into `api` (logo,name,price,diff,trade_num,trade_price,source,up_time,up_date) values ('%s','%s',%s,'%s',%s,%s,'%s',%s,'%s')" %(temp['logo'],temp['name'],temp['price'],temp['diff'],temp['tradeNum'],temp['tradePrice'],temp['from'],temp['upTime'],temp['upDate'])
			# print(sqls)
			db = Db()
			if db.ddl(sqls) > 0:
				# print(sqls)
				print( '%s --- 采集成功 \n'%(temp['name']) )
			# break
		return tepList

if __name__ == '__main__':
  Api()
