import urllib, json
import requests
import cv2
import csv
import time 
import os
from pandas import DataFrame

def analysis_Attribute(image_path):
	api_key = "piN66x5WUrRRV2PGrnM7hhJ1f-uzi8Nk"
	api_secret = "c1ZpOApLOxVe6j9Y-IJ7uDnP3iPME1Vs"
	detect_utl = "https://api-us.faceplusplus.com/facepp/v3/detect"

	data1={ "api_key": api_key,"api_secret":api_secret,"return_landmark":0, "return_attributes":"gender,age,ethnicity"}
	print(image_path)	
	files= {"image_file": open(image_path,'rb')}
	try:
		response=requests.post(detect_utl,data=data1,files=files)
		time.sleep(2)
		req_con=response.content.decode('utf-8')
		req_con = json.loads(req_con)		
		gender = req_con['faces'][0]['attributes']['gender']['value']
		age = req_con['faces'][0]['attributes']['age']['value']
		race = req_con['faces'][0]['attributes']['ethnicity']['value']
		print("Analysis Done")
		return gender,age,race
	except:
		print("No Face")
		return None,None,None


def writeExcel(image_list, gender_list, age_list,race_list,filename):
	data = {
	"image":image_list,
	"gender":gender_list,
	"age":age_list,
	"race":race_list
	}
	df=DataFrame(data)
	df.to_excel(filename)
	print("Finish Wirte Excel")

def processDirectory(dir_path):
	gender_list = []
	age_list = []
	image_list =[]
	race_list = []
	for image in os.listdir(dir_path):	
		gender,age, race= analysis(os.path.join(dir_path, image))		
		if gender is not None and age is not None and race is not None:
			image_list.append(image)
			gender_list.append(gender)
			age_list.append(age)
			race_list.append(race)
	writeExcel(image_list,gender_list,age_list, race_list, "filtered_statistic.xlsx")

def analysis_Landmark(image_path):
	api_key = "piN66x5WUrRRV2PGrnM7hhJ1f-uzi8Nk"
	api_secret = "c1ZpOApLOxVe6j9Y-IJ7uDnP3iPME1Vs"
	detect_utl = "https://api-us.faceplusplus.com/facepp/v3/detect"

	data1={ "api_key": api_key,"api_secret":api_secret,"return_landmark":1}
	print(image_path)	
	files= {"image_file": open(image_path,'rb')}
	try:
		response=requests.post(detect_utl,data=data1,files=files)
		time.sleep(2)
		req_con=response.content.decode('utf-8')
		req_con = json.loads(req_con)	
		landmark_info = req_con['faces'][0]["landmark"]
		res_list = []
		title = []
		for k,val in landmark_info.items():
			first_att  = k+"_y"
			second_att = k+"_x"
			res_list.append(val["y"])
			res_list.append(val["x"])
			title.append(first_att)
			title.append(second_att)
		print(title)
		print(res_list)
		# gender = req_con['faces'][0]['attributes']['gender']['value']
		# age = req_con['faces'][0]['attributes']['age']['value']
		# race = req_con['faces'][0]['attributes']['ethnicity']['value']
		# print("Analysis Done")
		# return gender,age,race
	except:
		print("No Face")
		return None,None,None


if __name__=="__main__":
	# path = "./filtered_faces"
	# gender_list = []
	# age_list = []
	# image_list =[]
	# race_list = []
	# for image in os.listdir(path):	
	# 	gender,age, race= analysisFacePlusPlus(os.path.join(path, image))		
	# 	if gender is not None and age is not None and race is not None:
	# 		image_list.append(image)
	# 		gender_list.append(gender)
	# 		age_list.append(age)
	# 		race_list.append(race)
	# writeExcel(image_list,gender_list,age_list, race_list, "filtered_statistic.xlsx")
	analysis_Landmark("./1.jpg")
