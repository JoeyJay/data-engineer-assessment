import requests
import json
import pandas as pd
import re
from typing import NamedTuple
from datetime import datetime

def gender_request(name, surname=None):
    url = 'https://innovaapi.aminer.cn/tools/v1/predict/gender?name={}+{}&org=Tsinghua'.format(name, surname)
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.text
    if response.status_code == 200:
        res = json.loads(result)
        gender = res.get('data').get('FGNL').get('gender')
        return gender

df = pd.read_csv('netflix_titles.csv')

#TODO trim names
#TODO automate devision of frames

def write_to_file(actor_obj):
    with open('actor_objects_V2.txt', 'a') as file1: 
        file1.write('\n{}'.format(str(actor_obj)))
        
        
def create_actor_obj(show_id, cast_list, index):
    for actor_name in cast_list:
        lname = None
        fname = None
        fname = actor_name.split()[0]
        if re.search(' ', actor_name): #  checking if they have a surname. Quick way
            lname = actor_name.split()[-1]
        gender = gender_request(fname, lname)
        actor_obj = (actor_name, gender, show_id)
        write_to_file(actor_obj)
        return actor_obj
    
    
def proc(dataframe):
   
    for index, row in dataframe.iterrows():
        show_id = dataframe['show_id'].loc[index]
        cast = str(dataframe['cast'].loc[index])
        cast = cast.split(',')
        create_actor_obj(show_id, cast, 0)
    

proc(df)