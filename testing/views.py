# Create your views here.
from django.http import HttpResponse
from math import sin, cos, sqrt, atan2, radians
from datetime import *
from time import *
from collections import defaultdict
import pdb
import re
import sys
from time import *  
import json
from server import settings
import simplejson
import operator
from pymongo import *
import ConfigParser 
import networkx as nx
# from logdb_graph import logdb_graph
import MySQLdb
import logging
import urllib
import urllib2
class API_helper: #View
	client = None
	plabrodb = None
	conn = None
	cur = None

	def __init__(self, configfile):

    	#GRANT ALL ON  *.* TO 'root'@'%' IDENTIFIED BY 'root';

		self.cur_stats = settings.cur_stats
		self.cur_plabro = settings.cur_plabro
		self.cur_engagement = settings.cur_engagement
		self.shoutscoll = settings.shoutscoll
		


	def get(self , request , *args , **kwargs):
		# Parse the request , call the producejson function and post it as httpresponse.
		# json_object = producejson(mob_num)
		print args , kwargs
		return HttpResponse("Hello , World !") # json_object

	def producejson(self , mob_num):

		query = 'SELECT  _id , phone , imei , ostype , osversion , appversion , phonemodel , registrationid , time , dev , invites FROM USERS WHERE phone = '
		query += '"'
		query += mob_num
		query += '"' 
		self.cur_plabro.execute(query)
		user_details = self.cur_plabro.fetchone()	

		# print len(user_details)

		# Everything in USERS #
		_id = user_details[0] 
		phone = user_details[1]
		imei = user_details[2]
		ostype = user_details[3]
		osversion = user_details[4]
		appversion = user_details[5]
		phonemodel = user_details[6]
		registrationid = user_details[7]
		time = user_details[8]
		dev = user_details[9]
		invites = user_details[10]
		# DONE #


		### -------- Get stats using the _id Somehow ---------- ###

		# Whatever happened to this.

		query = 'SELECT RT , TYPE , subtype , authkey , userid , usertype , time , session_id , querytime FROM CLIENTLOG1 WHERE userid = ' + phone
		self.cur_stats.execute(query)
		user_details = self.cur_stats.fetchall() 

	# 0 ----> RT
	# 1 ----> TYPE
	# 2 ----> subtype
	# 3 ----> authkey
	# 4 ----> userid (Mobile #)
	# 5 ----> usertype
	# 6 ----> time
	# 7 ----> sessionid
	# 8 ----> querytime

		groupbysession = {}

		for iterator in user_details :
			#print iterator[6]
			session = iterator[6].day , iterator[6].month , iterator[6].year
			#print session
		
			if session in groupbysession :
				groupbysession[session].append(iterator)

			else:
				groupbysession[session] = []
				groupbysession[session].append(iterator)

		########## SESSION == DAYS #####################################

		# Now groupbysession has all the stats grouped by days.

		for key , value in groupbysession.iteritems():
			#print "BREAKPOINT"
			# print key , value
			# key is the session
			# value contains the stats.
			sorted_value = sorted(value , key = lambda record : record[6])	# Sorting by timestamp.
			groupbysession[key] = sorted_value

		# Now the stats for everyday have been sorted by time.
		
		# Now Trying to display the sorted results :

		for key , value in groupbysession.iteritems():
			print "BREAKPOINT_SORTED_DAYS"
			print key  # , value
			# key is the session
			# value contains the stats for that session.
			for stat in value:
				timestamp_this = stat[6]
				RT_this = stat[0]
				subtype_this = stat[2]

				IST_time = timestamp_this.hour , timestamp_this.minute , timestamp_this.second

				print IST_time , RT_this , subtype_this

		
		############### GOT DAYS DATA FROM SHOUTS ###########################

		for k in xrange(100):
			print "New TEST"


		########## SESSION == SessionID #################################

	# 0 ----> RT
	# 1 ----> TYPE
	# 2 ----> subtype
	# 3 ----> authkey
	# 4 ----> userid (Mobile #)
	# 5 ----> usertype
	# 6 ----> time
	# 7 ----> session_id
	# 8 ----> querytime
	# 9 ----> Detail
	# 10 ----> Wifi Data (Optional)
		
		list_user_details = []

		for iterator in  user_details:

			iterator += ('Detail',)
			list_user_details.append(iterator)

		groupbysession_time = {}

		sorted_user_details = []

		old_sorted_user_details = sorted(list_user_details , key = lambda record : record[6])

		for iterator in old_sorted_user_details:
			if iterator[0] == 'WifiData':		############### SOME SHIT HERE ###########################
				
				pattern = '%Y-%m-%d %H:%M:%S'
				epoch = int(mktime(strptime(str(iterator[6]), pattern)))
				################## HAVE A LOOK #############################
				query = 'SELECT wifi FROM WIFILOG1 WHERE userid = ' + phone + ' AND time = ' + str(epoch)
				print query
				self.cur_stats.execute(query)
				addendum = self.cur_stats.fetchall() 
				print addendum
				iterator = iterator + (addendum,)
				sorted_user_details.append(iterator)
			else :
				sorted_user_details.append(iterator)

		isfirst = True
		sessionnumber = 1
		prevtime = datetime.now()
		curr_session = 1
		session_now = ''
		
		# Using Session ID

		for iterator in sorted_user_details :
			#print iterator[6]
			#session = iterator[6].day , iterator[6].month , iterator[6].year
			#print session
			if isfirst :
				prevtime = iterator[6] 
				isfirst = False
				stri = 'session' + str(sessionnumber)
				session_now = iterator[7]

				groupbysession_time[curr_session] = []
				groupbysession_time[curr_session].append(iterator)			
				curr_session = sessionnumber
				sessionnumber += 1

			else :

				difftime = iterator[6] - prevtime
				prevtime = iterator[6]
				diff_sec = difftime.total_seconds()

				if session_now == iterator[7] :
					groupbysession_time[curr_session].append(iterator)

				else :
					stri = 'session' + str(sessionnumber)
					curr_session = sessionnumber
					session_now = iterator[7]
					groupbysession_time[curr_session] = []
					groupbysession_time[curr_session].append(iterator)

					sessionnumber += 1
		
		# To Group by Timediff.
		'''
		for iterator in sorted_user_details :
			#print iterator[6]
			#session = iterator[6].day , iterator[6].month , iterator[6].year
			#print session
			if isfirst :
				prevtime = iterator[6] 
				isfirst = False
				stri = 'session' + str(sessionnumber)

				groupbysession_time[curr_session] = []
				groupbysession_time[curr_session].append(iterator)			
				curr_session = sessionnumber
				sessionnumber += 1

			else :

				difftime = iterator[6] - prevtime
				prevtime = iterator[6]
				diff_sec = difftime.total_seconds()

				if diff_sec < 600 :
					groupbysession_time[curr_session].append(iterator)

				else :
					stri = 'session' + str(sessionnumber)
					curr_session = sessionnumber
					groupbysession_time[curr_session] = []
					groupbysession_time[curr_session].append(iterator)

					sessionnumber += 1
		'''
		groupbysession_time_sorted = sorted(groupbysession_time.items(), key= lambda x : x[0])

		for iterator in groupbysession_time_sorted:
			
			#print "BREAKPOINT"
			# print key , value
			# key is the session
			# value contains the stats.
			key , value = iterator
			print "BREAKPOINT_SORTED_TIME"
			print key  # , value
			# key is the session
			# value contains the stats for that session.
			for stat in value:
				timestamp_this = stat[6]
				RT_this = stat[0]
				subtype_this = stat[2]
				sessionID_this = stat[7]

				IST_time = timestamp_this.hour , timestamp_this.minute , timestamp_this.second

				print IST_time , RT_this , subtype_this , sessionID_this

		################# GOT SORTED TIME GAP DATA #####################

		for k in xrange(100):
			print "No More Breakpoints"


		##############################################################
		### -------- Accessing the ENGAGEMENTS table ----------- ###

		query = 'SELECT * FROM ENGAGEMENT WHERE user_id = ' + str(_id)
		self.cur_engagement.execute(query)
		user_details = self.cur_engagement.fetchall()

	# 0 -----> _id      
	# 1 -----> user_id  
	# 2 -----> message  
	# 3 -----> operator 
	# 4 -----> medium   
	# 5 -----> shout_id 
	# 6 -----> comments 
	# 7 -----> time
	# 8 -----> Engagement

		list_user_engagements = []

		for iterator in  user_details:
			iterator += ('Engagement',)
			print iterator
			list_user_engagements.append(iterator)

		for k in xrange(100):
			print "No More Breakpoints FUCK OFF"

		list_user_engagements_sorted = sorted(list_user_engagements, key = lambda x : x[7])

		i = 0
		j = 0
		k= 0
		new_final_I_HOPE_sorted_list = []
		while(1):

			print i,j,k

			if (i == len(sorted_user_details)) and (j == len(list_user_engagements_sorted)):
				break
			if (i == len(sorted_user_details)):
				while (j < len(list_user_engagements_sorted)):
					new_final_I_HOPE_sorted_list.insert( k , list_user_engagements_sorted[j])
					k += 1
					j += 1

			elif (j == len(list_user_engagements_sorted)):
				while (i < len(sorted_user_details)):
					new_final_I_HOPE_sorted_list.insert( k , sorted_user_details[i])
					k += 1
					i += 1
			
			else:
				print sorted_user_details[i]
				ith = (sorted_user_details[i])[6]
				jth = (list_user_engagements_sorted[j])[7]

				if( ith < jth ):
					new_final_I_HOPE_sorted_list.insert(k , sorted_user_details[i])
					i += 1
					k += 1
				elif(ith == jth):
					new_final_I_HOPE_sorted_list.insert(k , sorted_user_details[i])
					i += 1
					k += 1
				else:
					new_final_I_HOPE_sorted_list.insert(k , list_user_engagements_sorted[j])
					j += 1
					k += 1

		for element in new_final_I_HOPE_sorted_list:
			print element

			groupbysession_final_days = {}

			# iterator is a mix of two kinds of objects.

		for iterator in new_final_I_HOPE_sorted_list:
			
			if len(iterator) == 9:
				session = str(iterator[7].day) + '/' +  str(iterator[7].month) + '/' + str(iterator[7].year)
				lis = list(iterator)
				lis[7] = str(lis[7])
				iterator = tuple(lis)	
			else:
				session = str(iterator[6].day) + '/' + str(iterator[6].month) + '/' + str(iterator[6].year)
				lis = list(iterator)
				lis[6] = str(lis[6])
				iterator = tuple(lis)	
			if session in groupbysession_final_days :
				groupbysession_final_days[session].append(iterator)

			else:
				groupbysession_final_days[session] = []
				groupbysession_final_days[session].append(iterator)

	#	for iterator in new_final_I_HOPE_sorted_list :
	#		
	#		if len(iterator) == 9:
	#			session = str(iterator[7].day) + '/' +  str(iterator[7].month) + '/' + str(iterator[7].year)
	#		else:
	#			session = str(iterator[6].day) + '/' + str(iterator[6].month) + '/' + str(iterator[6].year)
	#	
	#		if session in groupbysession_final_days :
	#			groupbysession_final_days[session].append(iterator)
	#
	#		else:
	#			groupbysession_final_days[session] = []
	#			groupbysession_final_days[session].append(iterator)

		for k in xrange(100):
			print "UEQFI"

		print groupbysession_final_days

			### This has the all the activity log of thge guy ... ###
		self.return_dict = {}
		self.return_dict['final_json_object_timeline'] = groupbysession_final_days


		############################################################





		################################################################

		### Getting Elastic Data ###
		
		## The following three lines ##
		#hit_url = 'http://code.plabro.com:9200/upf_count/profile_feature_count/' + str(_id)		# To get stuff from elastic search
		#response = urllib2.urlopen(hit_url)
		#data = json.load(response)   # data contains the json result.
		## END ##

		#print data
		
		### Got this data too !!!!! ###

		###############################################################	
		
		shouts_unfiltered = self.shoutscoll.find({"authorid":_id})

		shouts = []

		for unfiltered in shouts_unfiltered:
			if unfiltered.get('delete',0) == 0 and unfiltered.get('ignore',0) == 0 :
				shouts.append(unfiltered)
		
		# shouts is a list that has the Shouts ... Process it according to 'flavor'
		
		num_shouts = len(shouts)
		
		print "Total =" , num_shouts

		dict_records = {}
		
		# Count of stuff
		dict_records['past_day_avail'] = 0
		dict_records['past_day_req'] = 0
		dict_records['past_week_avail'] = 0
		dict_records['past_week_req'] = 0
		dict_records['past_month_avail'] = 0
		dict_records['past_month_req'] = 0
		dict_records['all_avail'] = 0
		dict_records['all_req'] = 0

		# Data of stuff
		dict_records['past_day_avail_list'] = []
		dict_records['past_day_req_list'] = []
		dict_records['past_week_avail_list'] = []
		dict_records['past_week_req_list'] = []
		dict_records['past_month_avail_list'] = []
		dict_records['past_month_req_list'] = []
		dict_records['all_avail_list'] = []
		dict_records['all_req_list'] = []

		for iterator in shouts:
			availability = iterator.get('avail_req' , '')
			#print iterator.get('time',datetime.now())
			t1 = iterator.get('time',datetime.now())  # Dont know what to give as the optional parameter.
			t2 = datetime.now()
			#print t1
			#print t2
			timedelta = t2-t1	
			
			days =  timedelta.days
			# seconds = timedelta.total_seconds()

			# print days , seconds

			temp = iterator["time"]
			temp = str(temp)
			iterator["time"] = temp

			if len(availability) > 0:
				
				if "Available" in availability :
					if days < 1:
						dict_records['past_day_avail'] += 1
						dict_records['past_week_avail'] += 1
						dict_records['past_month_avail'] += 1
						dict_records['all_avail'] += 1

						dict_records['past_day_avail_list'].append(iterator)
						dict_records['past_week_avail_list'].append(iterator)
						dict_records['past_month_avail_list'].append(iterator)
						dict_records['all_avail_list'].append(iterator)
					
					if days < 7:
						dict_records['past_week_avail'] += 1
						dict_records['past_month_avail'] += 1
						dict_records['all_avail'] += 1

						dict_records['past_week_avail_list'].append(iterator)
						dict_records['past_month_avail_list'].append(iterator)
						dict_records['all_avail_list'].append(iterator)
					
					if days < 30:
						dict_records['past_month_avail'] += 1
						dict_records['all_avail'] += 1

						dict_records['past_month_avail_list'].append(iterator)
						dict_records['all_avail_list'].append(iterator)

					else:
						dict_records['all_avail'] += 1
				
						dict_records['all_avail_list'].append(iterator)

				else:						# If it's not availability then ...
					if days < 1:
						dict_records['past_day_req'] += 1
						dict_records['past_week_req'] += 1
						dict_records['past_month_req'] += 1
						dict_records['all_req'] += 1

						dict_records['past_day_req_list'].append(iterator)
						dict_records['past_week_req_list'].append(iterator)
						dict_records['past_month_req_list'].append(iterator)
						dict_records['all_req_list'].append(iterator)

					if days < 7:
						dict_records['past_week_req'] += 1
						dict_records['past_month_req'] += 1
						dict_records['all_req'] += 1

						dict_records['past_week_req_list'].append(iterator)
						dict_records['past_month_req_list'].append(iterator)
						dict_records['all_req_list'].append(iterator)

					if days < 30:
						dict_records['past_month_req'] += 1
						dict_records['all_req'] += 1

						dict_records['past_month_req_list'].append(iterator)
						dict_records['all_req_list'].append(iterator)

					else:
						dict_records['all_req'] += 1

						dict_records['all_req_list'].append(iterator)

			else:
				print "The !?"

		self.return_dict['final_json_object_stat'] = dict_records
		self.return_dict_json = json.dumps(self.return_dict , ensure_ascii=False)
		return self.return_dict_json

		
		# print dict_records
		# Now for the ones during the past one day
		# shoutsinfo.get('locktime',datetime.now())


def process(request , *args , **kwargs):
	# Assumption : mob_num is valid , no exception handling done here.

	mob_num = kwargs['mob_num']
	configfile = "stats1.cfg"
	hk = API_helper(configfile)
	json_object =  hk.producejson(mob_num)	
	
	return HttpResponse(json_object)
	
	#if mobile[:3] != '+91':
	#	return HttpResponse('This page shows a list of most recent posts.')
	#else:
	#	return HttpResponse(API_helper())



#if __name__ == '__main__':
#	if len(sys.argv) > 1:
#		configfile = sys.argv[1]
#		mob_num = sys.argv[2]
#	hk = API_helper(configfile)
#	hk.producejson(mob_num)