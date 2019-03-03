import cv2
import numpy as np
import matplotlib.pyplot as plt

class Detection:
    """
    face detection class
    """
    def __init__(self):
        self.classifier = "./haarcascade_frontalface_default.xml"

    def detection(self, image):
        """
        :param image (numpy array)
        :return: the cropped image (numpy array)
        """

        face_cascade = cv2.CascadeClassifier(self.classifier)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.15,
            minNeighbors=5,
            minSize=(5, 5),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        if len(faces) >= 1:
            areas = []
            for box in faces:
                (x, y, w, h) = box
                areas.append(w * h)
            (x, y, w, h) = faces[areas.index(max(areas))]

            axis_hori = int(0.5 * w)
            axis_vert = int(h * 0.6)

            white_image = np.ones_like(image) * 255
            mask = np.zeros_like(image)
            center_x, center_y = (int((x + x + w) / 2), int((y + y + h) / 2))
            print(center_x,center_y)
            origin_y, origin_x, _ = mask.shape
            y_start = max([0, center_y - axis_vert])
            y_end = min([origin_y, center_y + axis_vert])
            x_start = max([0, center_x - axis_hori])
            x_end = min([origin_x, center_x + axis_hori])
            center_x,center_y = (int((x_start+x_end)/2),int((y_start+y_end)/2))
            print(center_x, center_y)
            mask = cv2.ellipse(mask, center=(center_x, center_y), axes=(int((x_end-x_start)/2), int((y_end-y_start)/2)), angle=0,startAngle=0, endAngle=360, color=(255, 255, 255), thickness=-1)
            back_ground_mask = 255 - mask
            result = np.bitwise_and(image, mask)
            back_ground = np.bitwise_and(white_image, back_ground_mask)
            result += back_ground

            result = result[y_start:y_end, x_start:x_end]

            new_x, new_h, _ = result.shape
            # result = cv2.resize(result, (228, 256))
            return result, new_x, new_h
        else:
            return None