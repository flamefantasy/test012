#coding:utf-8
import unittest
import json
import HtmlTestRunner
from demo import RunMain



class TestMethod(unittest.TestCase):
	
	
	def setUp(self):
	
		self.run = RunMain()
	
	def test_01(self):
		data = {
		'userId':'bf28e175219d47b1ae8384de50493052',
		'access_token':'1352467890bqfy',
		'pageSize':'100',
		'pageIndex':'1'
		}
		url='https://y3zhbh5.zhbservice.com/h5service/personal/productFavoriteList'
			
		#run=RunMain(url,'POST',data)
		res = self.run.run_main(url,'POST',data)
		#print (res)
		self.assertEqual(res['access_token'],'1352467890bqfy',"测试不通过")
		globals()['a']='123'
		'''
		if res['access_token']=='1352467890bqfy':
			print("测试通过")
		else:
			print("测试不通过")
		'''
	#@unittest.skip('test_02')
	def test_02(self):
		print(a)
		data = {
		'userId':'bf28e175219d47b1ae8384de50493052',
		'access_token':'1352467890bqfy',
		'pageSize':'100',
		'pageIndex':'1'
		}
		url='https://y3zhbh5.zhbservice.com/h5service/personal/productFavoriteList'
			
		#run=RunMain(url,'POST',data)
		res = self.run.run_main(url,'POST',data)
		#print (res)
		self.assertEqual(res['access_token'],'1352467890bqfy123',"测试不通过")
		'''
		if res['letterSource'=='123']:
			print("测试通过")
		else:
			print("测试不通过")
		'''
		#self.assertEqual(res['letterSource'],'ZHB',"测试失败")

if __name__ == '__main__':
	filepath = "../report/Htmlreport.html"
	fp = open(filepath,'wb')
	#unittest.main()
	suite = unittest.TestSuite()
	suite.addTest(TestMethod('test_01'))
	suite.addTest(TestMethod('test_02'))
	runner = HtmlTestRunner.HTMLTestRunner(output='fp',report_title='this is first report')
	runner.run(suite)
	#unittest.TextTestRunner().run(suite)
