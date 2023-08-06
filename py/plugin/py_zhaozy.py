#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider

class Spider(Spider):
	def getDependence(self):
		return ['py_ali']
	def getName(self):
		return "py_zhaozy"
	def init(self,extend):
		self.ali = extend[0]
		print("============py_zhaozy============")
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def homeContent(self,filter):
		result = {}
		return result
	def homeVideoContent(self):
		result = {}
		return result
	def categoryContent(self,tid,pg,filter,extend):
		result = {}
		return result
	header = {
		"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
		"Referer": "https://zhaoziyuan.la/"
	}
	def detailContent(self,array):
		tid = array[0]
		print(self.getName())
		pattern = '(https://www.aliyundrive.com/s/[^\"]+)'
		url = self.regStr(tid,pattern)
		if len(url) > 0:
			return self.ali.detailContent(array)

		rsp = self.fetch('https://zhaoziyuan.la/'+tid)
		url = self.regStr(rsp.text,pattern)
		if len(url) == 0:
			return ""
		newArray = [url]
		print(newArray)
		return self.ali.detailContent(newArray)

	def searchContent(self,key,quick):
		map = {
			'7':'文件夹',
			'1':'视频'
		}
		ja = []
		for tKey in map.keys():
			url = "https://zhaoziyuan.la/so?filename={0}&t={1}".format(key,tKey)
			rsp = self.fetch(url,headers=self.header)
			root = self.html(self.cleanText(rsp.text))
			aList = root.xpath("//li[@class='clear']//a")
			for a in aList:
				# title = a.xpath('./h3/text()')[0] + a.xpath('./p/text()')[0]
				title = self.xpText(a,'./h3/text()') + self.xpText(a,'./p/text()')
				pic = 'https://img0.baidu.com/it/u=603086994,1727626977&fm=253&fmt=auto?w=500&h=667'
				jo = {
					'vod_id': self.xpText(a,'@href'),
					'vod_name': '[{0}]{1}'.format(key,title),
					'vod_pic': pic
				}
				ja.append(jo)
		result = {
			'list':ja
		}
		return result

	def playerContent(self,flag,id,vipFlags):
		return self.ali.playerContent(flag,id,vipFlags)

	config = {
		"player": {},
		"filter": {}
	}
	header = {}

	def localProxy(self,param):
		return [200, "video/MP2T", action, ""]