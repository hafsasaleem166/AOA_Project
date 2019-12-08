import app as app
import cv2
import os
import numpy as np
import pymysql
from PIL import Image
import glob
import math
from flask import Flask, render_template, url_for, request


app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0
connection = pymysql.connect(host="localhost", user="root", passwd="", database="images")
cursor = connection.cursor()



@app.route("/")

@app.route("/index")
def show_index():
    return render_template('index.html')
@app.route("/about")
def show_about():
    return render_template('about.html')
@app.route("/Images Choosen")
def show_image():
    Image=images()
    return render_template('Images Choosen.html',imageUpload=Image)

def images():
    # path = glob.glob("./static/imagescopy/*.jpg")
    # print(len(path))
    # cv_img = []
    # for img in path:
    #     n = cv2.imread(img)
    #
    #     image_list=n.tolist()
    #     r = g = b = 0
    #     for row in image_list:
    #         for item in row:
    #             b = b + item[0]
    #             g = g + item[1]
    #             r = r + item[2]
    #     total = r + g + b
    #     i_red = r / total * 100
    #     i_green = g / total * 100
    #     i_blue = b / total * 100
    #     imgray = cv2.cvtColor(n, cv2.COLOR_BGR2GRAY)
    #     ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    #     contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #     print("Number of contours = " + str(len(contours)))
    #     print(img)
    #
    #
    #     edges = cv2.Canny(n, 100, 200)
    #     cv_img.append(n)
    #
    #     cursor.execute('INSERT INTO imagesdetail(Name, Red, Green,Blue,Contour,Edges) VALUES (%s,%s,%s, %s,%s,%s)',
    #                  (img, i_red, i_green, i_blue,str(len(contours)),str(len(edges))))
    Images=[]
    cursor.execute("SELECT Edges,Name,Red,Green,Blue,Contour FROM imagesdetail")

    myresult = cursor.fetchall()
    n = cv2.imread("chair.jpg")
    edges = cv2.Canny(n, 100, 200)
    image_list = n.tolist()
    r = g = b = 0
    for row in image_list:
        for item in row:
            b = b + item[0]
            g = g + item[1]
            r = r + item[2]
    total = r + g + b
    i_red = r / total * 100
    i_green = g / total * 100
    i_blue = b / total * 100


    imgray = cv2.cvtColor(n, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Number of contours = " + str(len(contours)))
    c=(len(contours),len(edges))
    xx =(i_red, i_green, i_blue)
    sortedd=[]
    for x in myresult:

        y=(float(x[2]),float(x[3]),float(x[4]))
        cc=(int(x[5]),int(x[0]))

        distancec = math.sqrt(sum([(a - b) ** 2 for a, b in zip(c, cc)]))
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(xx, y)]))
        sortedd.append((distance,distancec,x[1]))
        sortedd.sort()
    for x in sortedd[:20]:
        if x[0]<=5 and  x[0]>=0 and x[1]>=0 and x[1]<=3000:
            # image=cv2.imread(x[2])
            # cv2.imshow("image",image)
            Images.append(x[2])
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
    return Images


    # connection.commit()
    # connection.close()







if __name__ == "__main__":
    app.run()
