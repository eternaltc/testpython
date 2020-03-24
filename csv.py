from os import path
import os
import csv


path.exists("d:/a.txt")  #判断文件是否存在
os.mkdir("文件名")

with open("test.csv","w") as f:
    csv = csv.writer(f)
    csv.writerows(" ")
