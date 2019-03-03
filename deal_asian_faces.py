import cv2
import numpy as np
import matplotlib.pyplot as plt
from facedetector import FaceDetector
import os
import xlsxwriter

def save_height_width(filenames, widths, heights):
    filename = "./height_width_asianfaces.xlsx"
    workbook  = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet("AsianFaces")
    headings = ['File','Width','Height']
    worksheet.write_row('A1',headings)
    worksheet.write_column('A2',filenames)
    worksheet.write_column('B2',widths)
    worksheet.write_column('C2',heights)
    print("Saved to File={}".format(filename))


def dealAsian():
    detector = Detection()
    data_path  = "./AsianFacesV1Origin"
    data_out_path = "./asian faces version1/crop_unsatisfy/"
    data_out_path_satisfy = "./asian faces version1/crop_satisfy/"
    identities = os.listdir(data_path)
    new_filenames = []
    widths = []
    heights = []
    count = 0
    Faces = 0
    All = 0
    for classindex,person in enumerate(identities):
        dirpath = data_path+"/"+person
        if person != ".DS_Store" and person!="._.DS_Store":
            files = os.listdir(dirpath)
            for file in files:
                print("=============================")
                All += 1
                image = cv2.imread(dirpath+"/"+file)
                if image is not None:                    
                    print("Load Dir={} and Image={}".format(person,file))
                    res = detector.detection(image)
                    if res is not None:
                        Faces += 1
                        crop_image,w, h = res
                        #name="subject_"+str(classindex)+"_"+file                       
                        name = person + "_"+file
                        if w>=250:
                            count += 1
                            cv2.imwrite(data_out_path_satisfy+"/"+name,crop_image)
                        else:                            
                            cv2.imwrite(data_out_path+"/"+name,crop_image)
                        widths.append(w)
                        heights.append(h)
                    else:
                        print("No Faces")                    

                else:
                    print("Read Image Wrong....")
    print("Count/Faces/ALL={}/{}/{}".format(count,Faces,All))
    #save_height_width(new_filenames,widths,heights)


if __name__ == "__main__":
    dealAsian()
    print("Finish")

