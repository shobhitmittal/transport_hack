from django.db import models

class Station_name(models.Model):

	station_code=models.CharField(max_length=255,primary_key=True)
	station_name=models.CharField(max_length=255, unique=False)
	#operator=models.CharField(max_length=255, unique=False)
	#cid=models.CharField(max_length=255, unique=False)
	#called_number=models.CharField(max_length=255, unique=False)
	#event=models.CharField(max_length=255, unique=False)
	#time_stamp = models.DateTimeField(auto_now_add=True)

class Train_name(models.Model):

	train_code=models.CharField(max_length=255,primary_key=True)
	train_name=models.CharField(max_length=255,unique=False)
	#8 bit binary data
	class_aval=models.CharField(max_length=15,null=True)
	#7 bit binary data
	days_aval=models.CharField(max_length=15,null=True)

class Train_route(models.Model):

	route_id=models.AutoField(primary_key=True)
	train_code=models.ForeignKey(Train_name)
	src_station=models.ForeignKey(Station_name,related_name='train_src')
	dest_station=models.ForeignKey(Station_name,related_name='train_dest')
	depr_time=models.CharField(max_length=255,unique=False)
	arr_time=models.CharField(max_length=255,unique=False)
	distance=models.CharField(max_length=255,unique=False)
	duration=models.CharField(max_length=255,unique=False)

class Fare_route(models.Model):

	route_id=models.ForeignKey(Train_route)
	fc_fare=models.CharField(max_length=255,null=True)
	sl_fare=models.CharField(max_length=255,null=True)
	twos_fare=models.CharField(max_length=255,null=True)
	cc_fare=models.CharField(max_length=255,null=True)
	onea_fare=models.CharField(max_length=255,null=True)
	twoa_fare=models.CharField(max_length=255,null=True)
	threea_fare=models.CharField(max_length=255,null=True)
	threee_fare=models.CharField(max_length=255,null=True)

'''
class Hangup(models.Model):
	
	sid=models.CharField(max_length=255,primary_key=True)
	total_call_duration=models.CharField(max_length=255, unique=False)
	process=models.CharField(max_length=255, unique=False)
	cid=models.CharField(max_length=255, unique=False)
	called_number=models.CharField(max_length=255, unique=False)
	event=models.CharField(max_length=255, unique=False)
	message=models.TextField(null=False,default='empty')
	time_stamp = models.DateTimeField(auto_now_add=True)
	#hangup
	#{u'called_number': [u'911130803946'], u'cid': [u'8041169706'],
	#u'process': [u'none'], u'total_call_duration': [u'13'], u'sid': [u'1104528084751171'], u'event': [u'Hangup']}
	#Disconnection
	#{u'called_number': [u'911130803946'], u'cid': [u'8041169706'], u'process': [u'none'],
	# u'total_call_duration': [u'36'], u'sid': [u'9465281810416375'], u'message': [u'500 Internal Server Error'], u'event': [u'Disconnect']}

class dev(models.Model):

	dev_name=models.CharField(max_length=255,primary_key=True)
	access_token=models.TextField(null=False)
	expiry_date=models.CharField(max_length=255,null=False)
	time_stamp = models.DateTimeField(auto_now_add=True)
'''