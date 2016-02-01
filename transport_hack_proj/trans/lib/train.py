import requests
from trans import models
import libber
import time

def data_encoder(data,isclass=False):
	if isclass is False:
		pass
	elif isclass is True:
		pass
	else:
		 print 'Invalid value obtained for data_encoder funcation.Value Obtained is: '+str(isclass)

def fetch_pnr_status(pnr_no,railway_api):
	url_pnr='http://api.railwayapi.com/pnr_status/pnr/'+str(pnr_no)+'/apikey/'+str(railway_api)+'/'
	req_data_pnr= requests.get(url_pnr)
	if req_data_pnr and req_data_pnr.status_code==requests.codes.ok:
		data_json=req_data_pnr.json()
		data_return={}
		if str(data_json['response_code'])=='200':
			if str(data_json['error']).lower()=='false':
				data_return['data']=data_json
			elif str(data_json['error']).lower()=='true':
				data_return['error']='PNR Entered is Invalid.'
		else:
			data_return['error']='Some Error Occured, Please Try again.'
		return data_return

def fetch_train_names(data_gov_api_key,railway_api):
	flag= True
	data_return=[]
	count_offset=0
	url_lists=[]
	start=time.time()
	for count_offset in xrange(0,700):
		url='https://data.gov.in/api/datastore/resource.json?resource_id=b46200c1-ca9a-4bbe-92f8-b5039cc25a12&api-key='+str(data_gov_api_key)+'&offset='+str(count_offset)
		url_lists.append(url)
		print count_offset
	data_thread=libber.run_threads(url_lists)
	for data_req in data_thread:
		if data_req['records']:
			for data_req_save in data_req['records']:
				train_no_flag=str(data_req_save['Train No.'].split("'")[1])
				data_return.append(train_no_flag)
				print train_no_flag
				(station_code_save,station_code_status)= models.Station_name.objects.get_or_create(station_code= data_req_save['station Code'], defaults={'station_name':data_req_save['Station Name']})
				print (station_code_save,station_code_status)
				(train_code_save,train_code_status)= models.Train_name.objects.get_or_create(train_code= str(data_req_save['Train No.'].split("'")[1]), defaults={'train_name':data_req_save['train Name']})
				print (train_code_save,train_code_status)
				#print count_offset
			else:
				pass
	print len(data_return)
	print  time.time()-start
	status_code=[]
	status_code_false=[]
	data_return=list(set(data_return))
	url_lists=[]
	for train_no_data in data_return:
		print train_no_data
		url_1='http://api.railwayapi.com/route/train/'+str(train_no_data)+'/apikey/'+str(railway_api)+'/'
		print url_1
		url_lists.append(url_1)
	data_thread_1=libber.run_threads(url_lists,number_threads=10)
	for req_data_1 in data_thread_1:
		if str(req_data_1['response_code'])=='200':
			status_code.append(str(req_data_1['response_code']))
			(train_code_save,train_code_status)= models.Train_name.objects.get_or_create(train_code= str(req_data_1['train']['number']), defaults={'train_name':req_data_1['train']['name'],'class_aval':dummy_value,'days_aval':dummy_value_1})
			print (train_code_save,train_code_status)
		else:
			status_code_false.append(str(req_data_1['response_code']))
	return len(status_code),len(status_code_false)