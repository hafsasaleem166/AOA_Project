import cv2
from PIL import Image

img = cv2.imread('mobile.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255,0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
print(contours[0])

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.drawContours(imgray, contours, -1, (0, 255, 0), 3)

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread('mobile.jpg')
cv2.imshow("Image1", image)

image_list = image.tolist()
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
print("the percentage of red content=", i_red, "%")
print("the percentage of green content=", i_green, "%")
print("the percentage of blue content=", i_blue, "%")


def calculate_brightness(image):
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else brightness / scale


if __name__ == '__main__':
        image = Image.open("mobile.jpg")
        print(calculate_brightness(image))

