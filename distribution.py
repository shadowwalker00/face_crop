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
			# title.append(first_att)
			# title.append(second_att)
		# gender = req_con['faces'][0]['attributes']['gender']['value']
		# age = req_con['faces'][0]['attributes']['age']['value']
		# race = req_con['faces'][0]['attributes']['ethnicity']['value']
		print("Analysis Landmark Done")		
		return res_list
	except:
		print("No Face")
		return []

def processDir_landmark(dir_path):
	excel_data = ['mouth_upper_lip_left_contour2_y', 'mouth_upper_lip_left_contour2_x', 'mouth_upper_lip_top_y', 'mouth_upper_lip_top_x', 
	'mouth_upper_lip_left_contour1_y', 'mouth_upper_lip_left_contour1_x', 
	'left_eye_upper_left_quarter_y', 'left_eye_upper_left_quarter_x', 'left_eyebrow_lower_middle_y', 
	'left_eyebrow_lower_middle_x', 'mouth_upper_lip_left_contour3_y', 'mouth_upper_lip_left_contour3_x', 
	'right_eye_top_y', 'right_eye_top_x', 'left_eye_bottom_y', 'left_eye_bottom_x', 'right_eyebrow_lower_left_quarter_y', 
	'right_eyebrow_lower_left_quarter_x', 'right_eye_pupil_y', 'right_eye_pupil_x', 'mouth_lower_lip_right_contour1_y', 
	'mouth_lower_lip_right_contour1_x', 'mouth_lower_lip_right_contour3_y', 'mouth_lower_lip_right_contour3_x', 
	'mouth_lower_lip_right_contour2_y', 'mouth_lower_lip_right_contour2_x', 'contour_chin_y', 'contour_chin_x', 'contour_left9_y', 
	'contour_left9_x', 'left_eye_lower_right_quarter_y', 'left_eye_lower_right_quarter_x', 'mouth_lower_lip_top_y', 'mouth_lower_lip_top_x', 
	'right_eyebrow_upper_middle_y', 'right_eyebrow_upper_middle_x', 'left_eyebrow_left_corner_y', 
	'left_eyebrow_left_corner_x', 'right_eye_bottom_y', 'right_eye_bottom_x', 'contour_left7_y', 
	'contour_left7_x', 'contour_left6_y', 'contour_left6_x', 'contour_left5_y', 'contour_left5_x', 
	'contour_left4_y', 'contour_left4_x', 'contour_left3_y', 'contour_left3_x', 'contour_left2_y', 'contour_left2_x', 
	'contour_left1_y', 'contour_left1_x', 'left_eye_lower_left_quarter_y', 'left_eye_lower_left_quarter_x', 'contour_right1_y', 
	'contour_right1_x', 'contour_right3_y', 'contour_right3_x', 'contour_right2_y', 'contour_right2_x', 'mouth_left_corner_y', 
	'mouth_left_corner_x', 'contour_right4_y', 'contour_right4_x', 'contour_right7_y', 'contour_right7_x', 'right_eyebrow_left_corner_y', 
	'right_eyebrow_left_corner_x', 'nose_right_y', 'nose_right_x', 'nose_tip_y', 'nose_tip_x', 'contour_right5_y', 'contour_right5_x', 
	'nose_contour_lower_middle_y', 'nose_contour_lower_middle_x', 'left_eyebrow_lower_left_quarter_y', 'left_eyebrow_lower_left_quarter_x',
	'mouth_lower_lip_left_contour3_y', 'mouth_lower_lip_left_contour3_x', 'right_eye_right_corner_y', 'right_eye_right_corner_x', 
	'right_eye_lower_right_quarter_y', 'right_eye_lower_right_quarter_x', 'mouth_upper_lip_right_contour2_y', 
	'mouth_upper_lip_right_contour2_x', 'right_eyebrow_lower_right_quarter_y', 'right_eyebrow_lower_right_quarter_x', 
	'left_eye_left_corner_y', 'left_eye_left_corner_x', 'mouth_right_corner_y', 'mouth_right_corner_x', 'mouth_upper_lip_right_contour3_y',
	'mouth_upper_lip_right_contour3_x', 'right_eye_lower_left_quarter_y', 'right_eye_lower_left_quarter_x', 'left_eyebrow_right_corner_y', 
	'left_eyebrow_right_corner_x', 'left_eyebrow_lower_right_quarter_y', 'left_eyebrow_lower_right_quarter_x', 'right_eye_center_y', 
	'right_eye_center_x', 'nose_left_y', 'nose_left_x', 'mouth_lower_lip_left_contour1_y', 'mouth_lower_lip_left_contour1_x', 
	'left_eye_upper_right_quarter_y', 'left_eye_upper_right_quarter_x', 'right_eyebrow_lower_middle_y', 'right_eyebrow_lower_middle_x', 
	'left_eye_top_y', 'left_eye_top_x', 'left_eye_center_y', 'left_eye_center_x', 'contour_left8_y', 'contour_left8_x', 'contour_right9_y', 
	'contour_right9_x', 'right_eye_left_corner_y', 'right_eye_left_corner_x', 'mouth_lower_lip_bottom_y', 'mouth_lower_lip_bottom_x', 
	'left_eyebrow_upper_left_quarter_y', 'left_eyebrow_upper_left_quarter_x', 'left_eye_pupil_y', 'left_eye_pupil_x', 
	'right_eyebrow_upper_left_quarter_y', 'right_eyebrow_upper_left_quarter_x', 'contour_right8_y', 'contour_right8_x', 
	'right_eyebrow_right_corner_y', 'right_eyebrow_right_corner_x', 'right_eye_upper_left_quarter_y', 'right_eye_upper_left_quarter_x', 
	'left_eyebrow_upper_middle_y', 'left_eyebrow_upper_middle_x', 'right_eyebrow_upper_right_quarter_y', 'right_eyebrow_upper_right_quarter_x', 
	'nose_contour_left1_y', 'nose_contour_left1_x', 'nose_contour_left2_y', 'nose_contour_left2_x', 'mouth_upper_lip_right_contour1_y', 
	'mouth_upper_lip_right_contour1_x', 'nose_contour_right1_y', 'nose_contour_right1_x', 'nose_contour_right2_y', 'nose_contour_right2_x', 
	'mouth_lower_lip_left_contour2_y', 'mouth_lower_lip_left_contour2_x', 'contour_right6_y', 'contour_right6_x', 'nose_contour_right3_y', 
	'nose_contour_right3_x', 'nose_contour_left3_y', 'nose_contour_left3_x', 'left_eye_right_corner_y', 'left_eye_right_corner_x', 
	'left_eyebrow_upper_right_quarter_y', 'left_eyebrow_upper_right_quarter_x', 
	'right_eye_upper_right_quarter_y', 'right_eye_upper_right_quarter_x', 'mouth_upper_lip_bottom_y', 'mouth_upper_lip_bottom_x']

	excel_data_dict = {}
	for i in range(166):
		excel_data_dict["title"+str(i)] = []
	data = []
	data = [[] for i in range(166)]
	img_name = []
	for image in os.listdir(dir_path):
		res_list = analysis_Landmark(os.path.join(dir_path, image))
		# print(res_list)
		if len(res_list) != 0:
			img_name.append(image)
			for index, item in enumerate(res_list):
				temp = data[index]
				temp.append(item)
				data[index] = temp
	index = 0
	for k,val in excel_data_dict.items():
		excel_data_dict[k] = data[index]
		index += 1
	for k,v in excel_data_dict.items():
		
		if len(v)!=2:
			print(k)
			print(v)
	excel_data_dict["img"] = img_name
	df=DataFrame(excel_data_dict)
	df.to_excel("landmark_filter.xlsx")
	print("Finish Wirte Excel")

def test():
	excel_data = ['mouth_upper_lip_left_contour2_y', 'mouth_upper_lip_left_contour2_x', 'mouth_upper_lip_top_y', 'mouth_upper_lip_top_x', 
	'mouth_upper_lip_left_contour1_y', 'mouth_upper_lip_left_contour1_x', 
	'left_eye_upper_left_quarter_y', 'left_eye_upper_left_quarter_x', 'left_eyebrow_lower_middle_y', 
	'left_eyebrow_lower_middle_x', 'mouth_upper_lip_left_contour3_y', 'mouth_upper_lip_left_contour3_x', 
	'right_eye_top_y', 'right_eye_top_x', 'left_eye_bottom_y', 'left_eye_bottom_x', 'right_eyebrow_lower_left_quarter_y', 
	'right_eyebrow_lower_left_quarter_x', 'right_eye_pupil_y', 'right_eye_pupil_x', 'mouth_lower_lip_right_contour1_y', 
	'mouth_lower_lip_right_contour1_x', 'mouth_lower_lip_right_contour3_y', 'mouth_lower_lip_right_contour3_x', 
	'mouth_lower_lip_right_contour2_y', 'mouth_lower_lip_right_contour2_x', 'contour_chin_y', 'contour_chin_x', 'contour_left9_y', 
	'contour_left9_x', 'left_eye_lower_right_quarter_y', 'left_eye_lower_right_quarter_x', 'mouth_lower_lip_top_y', 'mouth_lower_lip_top_x', 
	'right_eyebrow_upper_middle_y', 'right_eyebrow_upper_middle_x', 'left_eyebrow_left_corner_y', 
	'left_eyebrow_left_corner_x', 'right_eye_bottom_y', 'right_eye_bottom_x', 'contour_left7_y', 
	'contour_left7_x', 'contour_left6_y', 'contour_left6_x', 'contour_left5_y', 'contour_left5_x', 
	'contour_left4_y', 'contour_left4_x', 'contour_left3_y', 'contour_left3_x', 'contour_left2_y', 'contour_left2_x', 
	'contour_left1_y', 'contour_left1_x', 'left_eye_lower_left_quarter_y', 'left_eye_lower_left_quarter_x', 'contour_right1_y', 
	'contour_right1_x', 'contour_right3_y', 'contour_right3_x', 'contour_right2_y', 'contour_right2_x', 'mouth_left_corner_y', 
	'mouth_left_corner_x', 'contour_right4_y', 'contour_right4_x', 'contour_right7_y', 'contour_right7_x', 'right_eyebrow_left_corner_y', 
	'right_eyebrow_left_corner_x', 'nose_right_y', 'nose_right_x', 'nose_tip_y', 'nose_tip_x', 'contour_right5_y', 'contour_right5_x', 
	'nose_contour_lower_middle_y', 'nose_contour_lower_middle_x', 'left_eyebrow_lower_left_quarter_y', 'left_eyebrow_lower_left_quarter_x',
	'mouth_lower_lip_left_contour3_y', 'mouth_lower_lip_left_contour3_x', 'right_eye_right_corner_y', 'right_eye_right_corner_x', 
	'right_eye_lower_right_quarter_y', 'right_eye_lower_right_quarter_x', 'mouth_upper_lip_right_contour2_y', 
	'mouth_upper_lip_right_contour2_x', 'right_eyebrow_lower_right_quarter_y', 'right_eyebrow_lower_right_quarter_x', 
	'left_eye_left_corner_y', 'left_eye_left_corner_x', 'mouth_right_corner_y', 'mouth_right_corner_x', 'mouth_upper_lip_right_contour3_y',
	'mouth_upper_lip_right_contour3_x', 'right_eye_lower_left_quarter_y', 'right_eye_lower_left_quarter_x', 'left_eyebrow_right_corner_y', 
	'left_eyebrow_right_corner_x', 'left_eyebrow_lower_right_quarter_y', 'left_eyebrow_lower_right_quarter_x', 'right_eye_center_y', 
	'right_eye_center_x', 'nose_left_y', 'nose_left_x', 'mouth_lower_lip_left_contour1_y', 'mouth_lower_lip_left_contour1_x', 
	'left_eye_upper_right_quarter_y', 'left_eye_upper_right_quarter_x', 'right_eyebrow_lower_middle_y', 'right_eyebrow_lower_middle_x', 
	'left_eye_top_y', 'left_eye_top_x', 'left_eye_center_y', 'left_eye_center_x', 'contour_left8_y', 'contour_left8_x', 'contour_right9_y', 
	'contour_right9_x', 'right_eye_left_corner_y', 'right_eye_left_corner_x', 'mouth_lower_lip_bottom_y', 'mouth_lower_lip_bottom_x', 
	'left_eyebrow_upper_left_quarter_y', 'left_eyebrow_upper_left_quarter_x', 'left_eye_pupil_y', 'left_eye_pupil_x', 
	'right_eyebrow_upper_left_quarter_y', 'right_eyebrow_upper_left_quarter_x', 'contour_right8_y', 'contour_right8_x', 
	'right_eyebrow_right_corner_y', 'right_eyebrow_right_corner_x', 'right_eye_upper_left_quarter_y', 'right_eye_upper_left_quarter_x', 
	'left_eyebrow_upper_middle_y', 'left_eyebrow_upper_middle_x', 'right_eyebrow_upper_right_quarter_y', 'right_eyebrow_upper_right_quarter_x', 
	'nose_contour_left1_y', 'nose_contour_left1_x', 'nose_contour_left2_y', 'nose_contour_left2_x', 'mouth_upper_lip_right_contour1_y', 
	'mouth_upper_lip_right_contour1_x', 'nose_contour_right1_y', 'nose_contour_right1_x', 'nose_contour_right2_y', 'nose_contour_right2_x', 
	'mouth_lower_lip_left_contour2_y', 'mouth_lower_lip_left_contour2_x', 'contour_right6_y', 'contour_right6_x', 'nose_contour_right3_y', 
	'nose_contour_right3_x', 'nose_contour_left3_y', 'nose_contour_left3_x', 'left_eye_right_corner_y', 'left_eye_right_corner_x', 
	'left_eyebrow_upper_right_quarter_y', 'left_eyebrow_upper_right_quarter_x', 
	'right_eye_upper_right_quarter_y', 'right_eye_upper_right_quarter_x', 'mouth_upper_lip_bottom_y', 'mouth_upper_lip_bottom_x']
	with open('mycsvfile.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(excel_data)


if __name__=="__main__":
	test()
