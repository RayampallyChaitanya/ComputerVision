import cv2
from imutils import build_montages
from imutils import paths
import random
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required= True, help="GIVE pics you IDiot")
ap.add_argument("-s", "--sample", type=int, default=21, help="Images")
args = vars(ap.parse_args())


image_path = list(paths.list_images(args["images"]))
random.shuffle(image_path)
image_path = image_path[:args["sample"]]


images = []

for image in image_path:
    img = cv2.imread(image)
    images.append(img)

montages = build_montages(images,(128,196), (7,3))


for montage in montages:
    cv2.imshow("montages", montage)
    cv2.waitKey(0)

