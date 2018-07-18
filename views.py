# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import courseblock_index,user_block_interaction
from django.http import HttpResponse,JsonResponse
import json
from django.core import serializers
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt  

@csrf_exempt
def completed(request):
	if request.method=="POST":
		block_id=request.POST.get('block_id')
		username=request.POST.get('username')

		x=user_block_interaction()
		
		result=dict()
		block=None
		user=User.objects.all()
		print(user)
		print(courseblock_index.objects.all())
		result=dict()
		result['message']="No user exists with given username"
		#check for existing users
		try:
			user=User.objects.get(username=username)
		except:
			result['message']="No user exists with given username"
			return HttpResponse(json.dumps(result), content_type="application/json",status=404)
			#return JsonResponse({"message": "No user exists with given username"}, 404)

		#check for valid block
		try:
			block=courseblock_index.objects.get(pk=block_id)
		except:
			result['message']="No block exists for given block id!"
			return HttpResponse(json.dumps(result), content_type="application/json",status=404)
			#return JsonResponse({"message": "No block exists for given block id!"}, 404)
		
		#check if given block is already completed

		exists=user_block_interaction.objects.filter(block__block_id=block_id,user__username=username)
		
		if not exists:
			x.user=user #change this to user aftwr changing the field to foreign key in models.py

			x.block=block
			x.block_number=block.block_number
			x.save()
			result['message']="Success"
			return HttpResponse(json.dumps(result), content_type="application/json",status=200)

			#return JsonResponse({'message': "success"}, 200)
		else:
			result['message']="User has already completed the given block"
			return HttpResponse(json.dumps(result), content_type="application/json",status=201)
			#return JsonResponse({'message': "User has already completed the given block"}, 200)

def get_progress(request):
	if request.method=="GET":
		course_id=request.GET.get('course_id')
		username=request.GET.get('username')
		result=dict()
		#result['completed_id']=[]
		result['completed_percent']=0
		result['last_completed_block_id']=''
		try:
			user=User.objects.get(username=username)
		except:
			result['message']="No user exists with given username"
			return HttpResponse(json.dumps(result), content_type="application/json",status=404)

			#return JsonResponse({'message': "No user exists with given username"}, 404)
			


		user_blocks=user_block_interaction.objects.filter(user__username=username,block__course_id=course_id)
		if not user_blocks:
			result['message']='No Progress in Given Course'
			res_json = json.dumps(result)
			return HttpResponse(res_json, content_type='application/json')
		else:
			total_blocks=courseblock_index.objects.filter(course_id=course_id)
			try:
				result['completed_percent']=round(((user_blocks.count()*1.0)/total_blocks.count())*100,2)
			except:
				result['completed_percent']=0

			result['completed_blocks']=list(user_blocks.values('block_number'))
			last_completed=list(user_blocks.order_by('-block_number')[:1])
			print(last_completed)
			result['last_completed_block_id']=last_completed[0].block.block_id
			result['message']='success'
			res_json = json.dumps(result)
			return HttpResponse(res_json, content_type='application/json')




