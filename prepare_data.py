import os
import csv

arr = os.listdir("imgs_fair/generated_imgs_fair/")
with open('test_images.csv', 'w') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(["img_path"])
    for img in arr:
        csvwriter.writerow([f"imgs_fair/generated_imgs_fair/{img}"])

