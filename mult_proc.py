import multiprocessing
import time
import requests
import json
import datetime
import re
import pandas as pd



result_list = []

class Process(multiprocessing.Process):

	def __init__(self, dataframe):
		super(Process, self).__init__()
		self.dataframe = dataframe
  
	def run(self):
		self.proc(self.dataframe)
		# print('some bull')
  
	def write_to_file(self, actor_obj):
		with open('actor_objects.txt', 'a') as file1: 
			file1.write('\n{}'.format(str(actor_obj)))
    
	def gender_request(self, name, lname):
		url = 'https://innovaapi.aminer.cn/tools/v1/predict/gender?name={}+{}&org=Tsinghua'.format(name, lname)
		payload={}
		headers = {}
		response = requests.request("GET", url, headers=headers, data=payload)
		result = response.text
		if response.status_code == 200:
			res = json.loads(result)
			gender = res.get('data').get('FGNL').get('gender')
			return gender

	def create_actor_obj(self, show_id, cast_list, index):
		for actor_name in cast_list:
			lname, fname = None, None
			fname = actor_name.split()[0]
			if re.search(' ', actor_name): #  checking if they have a surname. Quick way
				lname = actor_name.split()[-1]
			gender = self.gender_request(fname, lname)
			actor_obj = (actor_name, gender, show_id)
			self.write_to_file(actor_obj)
			result_list.append(actor_obj)
			#return actor_obj

	def proc(self, dataframe):      
		for index, row in dataframe.iterrows():
			show_id = dataframe['show_id'].loc[index]
			cast = str(dataframe['cast'].loc[index])
			cast = cast.split(',')
			self.create_actor_obj(show_id, cast, 0)

def caching(df, index):
    pass
 
def monitor():
    pass
	       
if __name__ == '__main__':
	df = pd.read_csv('file.csv')
	a = df.iloc[:10,:]
	b = df.iloc[11:21]
	c = df.iloc[22:33]
 
	p = Process(a) 
	p.start() 
	p.join() 
	p = Process(b) 
	p.start() 
	p.join()
	print(result_list)