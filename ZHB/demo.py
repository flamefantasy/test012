import requests
import json
class RunMain():
	'''
	def __init__(self,url,method,data=None):
		self.res = self.run_main(url,method,data)
	'''
	def send_get(self,url,data):
		res = requests.get(url=url,data=data).json()
		return json.dumps(res,indent=2,sort_keys=True)

	def send_post(self,url,data):
		res = requests.post(url=url,data=data).json()
		return json.dumps(res,indent=2,sort_keys=True)

	def run_main(self,url,method,data=None):
		res = None
		if method == 'GET':
			res = self.send_get(url,data)
		else:
			res = self.send_post(url,data)
		return json.loads(res)
	
if __name__ == '__main__':
	data = {
	'userId':'bf28e175219d47b1ae8384de50493052',
	'access_token':'1352467890bqfy',
	'pageSize':'100',
	'pageIndex':'1'
	}
	url='https://y3zhbh5.zhbservice.com/h5service/personal/productFavoriteList'
	run = RunMain()
	print (run.run_main(url,'POST',data))
#print (run.run_main(url,'POST',data))
