"""

Program to Parse through a json object and get the time it took to transfer each volume of instances.

Design Assumptions made:

1. The data size is bytes
2. The end time is always greater than start time
3. The timestamp on start time and end time remain in the same format throughout the file. %Y-%m-%d %H:%M:%S.%f+00:00
4. The json file is in the directory this program is in.

"""

import json
import datetime


with open("test.json") as f:											# Opening and reading json file
	json_data = json.load(f)
	
	for ele in json_data:												#Parsing through the entire object
		for ele_instances in ele["instances"]:							#Parsing through instances object
			for ele_volumes in ele_instances["volumes"]:				#Parsing through volumes object
				# reading the start time from json file and 
				# 	...  converting into a datetime object with format string mentioned.
				start_obj = datetime.datetime.strptime(ele_volumes["start_time"], "%Y-%m-%d %H:%M:%S.%f+00:00")
				end_obj   = datetime.datetime.strptime(ele_volumes["end_time"], "%Y-%m-%d %H:%M:%S.%f+00:00")
				# Getting the difference btw two datetime .
				# 	... Here we will get the difference btw two datetime objects no matter which day they are. 
				#	... The only pre-requisite is the end_time should be greater in terms of date than start_time
				#	... If the end_time is dated before the start time, we discard that volume. 

				if end_obj > start_obj:						# Just an extra check to only parse valid end times. 
					diff = (end_obj - start_obj).total_seconds() 

					print ("The time taken to transfer the volume "+ ele_volumes["tgt_name"] + " is "+ str(int(diff/60)) + " minutes "+str(diff%60) + " seconds")
					print ("The data transfer rate is " + str(float(ele_volumes["size"]) / (1024*1024*diff) ) + " MB/s" )