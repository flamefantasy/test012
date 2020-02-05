#coding:utf-8
from util.operation_excel import OperationExcel
from ZHB.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse

class DependentData:
	def __init__(self):
		self.case_id = case_id
		self.operation_excel = OperationExcel()
		self.data = GetData()
	#通过case-id去获取case的整行数据
	def get_case_line_data(self,case_id):
		rows_data = self.operation_excel.get_row_data(self.case_id)
		return rows_data

	#执行依赖测试，获取结果
	def run_dependent(self):
		run_method = RunMethod()
		row_num = self.operation_excel.get_row_num(self.case_id)
		request_data = self.data.get_data_for_json(row_num)
		header = self.data.is_header(row_num)
		method = self.data.get_request_method(row_num)
		url = self.data.get_request_url(row_num)
		res = run_method.run_main(method,url,request_data,header)
		return res

	#根据依赖的key去获取执行依赖测试case的响应，然后返回
	def get_data_for_key(self,row):
		depend_data = self.get_depend_key(row)
		response_data = self.run_dependent()
		json_exe = parse(depend_data)
		madle = json_exe.find(response_data)
		return [math.value for math in madle][0]


