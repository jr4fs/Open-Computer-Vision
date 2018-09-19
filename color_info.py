import cv2
import glob
import numpy as np

#Takes in a list of pixel values and prints information about them
def im_stats(list):
    first_val = []
    second_val = []
    third_val = []
    for x in list:
        first_val.append(x[0])
        second_val.append(x[1])
        third_val.append(x[2])
    first_val.sort()
    second_val.sort()
    third_val.sort()
    val1 = np.asarray(first_val)
    val2 = np.asarray(second_val)
    val3 = np.asarray(third_val)
    print("Average val[0]:" + str(np.mean(val1)))
    print("STD val[0]:" + str(np.std(val1)))
    print("val[0] Q1: " + str(first_val[(int)(len(first_val) * 0.25)]) + "\tval[0] Q3: " + str(first_val[(int)(len(first_val) * 0.75)]))
    print()

    print("Average val[1]:" + str(np.mean(val2)))
    print("STD val[1]:" + str(np.std(val2)))
    print("val[1] Q1: " + str(second_val[(int)(len(second_val) * 0.25)]) + "\tval[1] Q3: " + str(second_val[(int)(len(second_val) * 0.75)]))

    print()

    print("Average val[2]:" + str(np.mean(val3)))
    print("STD val[2]:" + str(np.std(val3)))
    print("val[2] Q1: " + str(third_val[(int)(len(third_val) * 0.25)]) + "\tval[2] Q3: " + str(third_val[(int)(len(third_val) * 0.75)]))

#appends to rgbs and hsvs the pixel values in all the images of dir_path
def im_info(dir_path, rgbs, hsvs):
    for filename in glob.glob(dir_path + "/*.jpg") + glob.glob(dir_path + "/*.png"):
        print("loaded " + filename)
        img = cv2.imread(filename)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                rgbs.append(img[x][y])
                hsvs.append(hsv[x][y])

rgbs = []
hsvs = []

im_info("truckShadows", rgbs, hsvs)
print()
print("RGB:")
im_stats(rgbs)
print("\n\nHSV:")
im_stats(hsvs)