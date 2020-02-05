#coding:utf-8

from util.operation_excel import OperationExcel
from data.data_config import *
from util.operation_json import OperetionJson
class GetData:
	def __init__(self):
		self.opera_excel = OperationExcel()

	#获取Excel行数，case个数
	def get_case_lines(self):
		return self.opera_excel.get_lines()

	#获取是否执行
	def get_is_run(self,row):
		flag = None
		col = int(get_run())
		run_model = self.opera_excel.get_cell_value(row,col)
		if run_model =='yes':
			flag = True
		else:
			flag = False
		return flag

	#是否携带header
	def is_header(self,row):
		col = int(get_header())
		header = self.opera_excel.get_cell_value(row,col)
		if header == 'yes':
			return get_header_value()
		else:
			return None

	#获取请求方式
	def get_request_method(self,row):
		col = int(get_run_way())
		request_method = self.opera_excel.get_cell_value(row,col)
		return request_method

	#获取URL
	def get_request_url(self,row):
		col = int(get_url())
		url = self.opera_excel.get_cell_value(row,col)
		return url

	#获取请求数据
	def get_request_data(self,row):
		col = int(get_data())
		data = self.opera_excel.get_cell_value(row,col)
		if data == '':
			return None
		return data

	#从json里获取数据
	def get_data_for_json(self,row):
		opera_json = OperetionJson()
		request_data = opera_json.get_data(self.get_request_data(row))
		return request_data

	#获取预期结果
	def get_expcet_data(self,row):
		col = int(get_expect())
		expect = self.opera_excel.get_cell_value(row,col)
		if expect == '':
			return None
		return expect

	#写入excel
	def write_result(self,row,value):
		col = int(get_result())
		self.opera_excel.write_value(row,col,value)

	#获取依赖数据的key
	def get_depend_key(self,row):
		col = int(get_data_depend())
		depend_key = self.opera_excel.get_cell_value(row,col)
		if depend_key == "":
			return None
		else:
			return depend_key

	#判断是否有Case依赖
	def is_depend(self,row):
		col = int(get_field_depend())
		depend_case_id = self.opera_excel.get_cell_value(row,col)
		if depend_case_id == "":
			return None
		else:
			return depend_case_id

	#获取数据依赖字段
	def get_depend_field(self,row):
		col = int(self.get_field_depend())
		data = self.opera_excel.get_cell_value(row,col)
		if data == "":
			return None
		else:
			return data