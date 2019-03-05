import urllib, json
import requests
import cv2
import csv
import time 
import os
from pandas import DataFrame

def analysis(image_path):
	api_key = "piN66x5WUrRRV2PGrnM7hhJ1f-uzi8Nk"
	api_secret = "c1ZpOApLOxVe6j9Y-IJ7uDnP3iPME1Vs"
	detect_utl = "https://api-us.faceplusplus.com/facepp/v3/detect"

	data1={ "api_key": api_key,"api_secret":api_secret,"return_landmark":0, "return_attributes":"gender,age"}
	print(image_path)	
	files= {"image_file": open(image_path,'rb')}
	try:
		response=requests.post(detect_utl,data=data1,files=files)
		time.sleep(2)
		req_con=response.content.decode('utf-8')
		req_con = json.loads(req_con)		
		gender = req_con['faces'][0]['attributes']['gender']['value']
		age = req_con['faces'][0]['attributes']['age']['value']
		print("Analysis Done")
		return gender,age
	except:
		print("No Face")
		return None,None


def writeExcel(image_list, gender_list, age_list):
	data = {
	"image":image_list,
	"gender":gender_list,
	"age":age_list
	}
	df=DataFrame(data)
	df.to_excel("new.xlsx")
	print("Finish Wirte Excel")


if __name__=="__main__":
	path = "/Users/chenguanghao/Desktop/test/"
	gender_list = []
	age_list = []
	image_list =[]
	for image in os.listdir(path):	
		gender,age = analysis(path+image)		
		if gender is not None and age is not None:
			image_list.append(image)
			gender_list.append(gender)
			age_list.append(age)
	writeExcel(image_list,gender_list,age_list)
