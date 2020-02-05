#coding:utf-8
import json

#fb = open("../dataconfig/collection.json")
#data = json.load(fb)
#print(data['collection'])

class OperetionJson:

	def __init__(self):
	    self.data = self.read_data()

	#读取JSON文件
	def read_data(self):
		with open('../dataconfig/collection.json') as fp:
			data = json.load(fp)
			return data

	#根据关键字获取数据
	def get_data(self,id):
		#print(id)
		return self.data[id]
 
if __name__ == '__main__':
	opjson = OperetionJson()
	print(opjson.get_data('collection'))