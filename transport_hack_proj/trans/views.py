from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse 
from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Context
import models
from django.conf import settings
import os
import json
import time
import re
from lib import train

def api_v1_rlwy_parse(request):
	if request.method=='GET':
		print request.GET
		data_gov_api_key=settings.DATA_GOV_API_KEY
		railway_api=settings.RAILWAY_API
		value=train.fetch_train_names(data_gov_api_key,railway_api)
		return HttpResponse('Heelo'+str(value))

def home_page(request):
	if request.method=='GET':
		print request.GET
		template_context = {'pnr_data': pnr_data}
		return render_to_response('home_page.html', template_context, context_instance=RequestContext(request))

def get_pnr_status(request):
	if request.method=='POST':
		print method.POST
		pnr_data=fetch_pnr_status(request.method['pnr_no'],railway_api)
		template_context = {'pnr_data': pnr_data}
		return render_to_response('pnr_data.html', template_context, context_instance=RequestContext(request))
	else:
		return HttpResponse('Request method is not permitted.Request Method is: '+str(request.method))

