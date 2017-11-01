# coding:utf-8
import os
import glob
import numpy as np
from PIL import Image
import codecs
# import cv2
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

# name = input("What is your name? ")

DATA_PATH = "/home/neo/Dataset/ICDAR2015/TextLocalization/TextLocalization_test_images"

image_list = glob.glob(os.path.join(DATA_PATH, '*.jpg'))
labelPath = "/home/neo/TFtoys/EAST/result"


# 标签文件既有坐标也有内容且一起显示
def show_all_with_label():
    for image in image_list:
        label_file_name = os.path.join(labelPath, "res_" + image.split('/')[-1][:-4] + '.txt')
        im = Image.open(image)
        im = np.array(im).astype(np.uint8)
        plt.imshow(im)
        labels = codecs.open(label_file_name, 'r', 'utf8').readlines()

        for label in labels:
            label = label.strip().split(',')
            LL = label[:-2]
            location = [int(i) for i in LL]
            context = label[-1].strip('"')
            # print(location)
            plt.plot([location[0], location[2], location[4], location[6], location[0]], [
                     location[1], location[3], location[5], location[7], location[1]], 'r-')
            # ,bbox={'facecolor':'white', 'alpha':0.5}
            plt.text(location[0], location[1], context, fontsize=8, color='#33FF36')
        plt.show()
        name = input("Continue? ")
        if name == 'n' or name == 'no':
            break


# 标签文件只有坐标，没有内容
def show_all_box():
    for image in image_list:
        label_file_name = os.path.join(labelPath, "res_" + image.split('/')[-1][:-4] + '.txt')
        im = Image.open(image)
        im = np.array(im).astype(np.uint8)
        plt.imshow(im)
        boxes = codecs.open(label_file_name, 'r', 'utf8').readlines()

        for box in boxes:
            box = box.strip().split(',')
            location = [int(i) for i in box]
            # print(location)
            plt.plot([location[0], location[2], location[4], location[6], location[0]], [
                     location[1], location[3], location[5], location[7], location[1]], 'r-')
            # ,bbox={'facecolor':'white', 'alpha':0.5}
            # plt.text(location[0], location[1], context, fontsize=8, color='#33FF36')
        plt.show()
        name = raw_input("Continue?")
        if name == 'n' or name == 'no':
            break


# 显示指定标号的box和内容标签
def show_num_with_box(num):
    img_name = 'image_' + str(num) + '.jpg'
    for image in image_list:
        if img_name in image:
            label_file_name = image[:-4] + '.txt'
            im = Image.open(image)
            im = np.array(im).astype(np.uint8)
            plt.imshow(im)
            labels = open(label_file_name, 'r', encoding='utf8').readlines()

            for label in labels:
                label = label.strip().split(',')
                LL = label[:-2]
                location = [int(i) for i in LL]
                context = label[-1].strip('"')
                # print(location)
                plt.plot([location[0], location[2], location[4], location[6], location[0]], [
                         location[1], location[3], location[5], location[7], location[1]], 'r-')
                plt.plot(location[0], location[1], 'b*')
                # ,bbox={'facecolor':'white', 'alpha':0.5}
                plt.text(location[0], location[1], context, fontsize=8, color='#33FF36')
            plt.show()


if __name__ == '__main__':
    # n = int(input("num"))
    # show_num(n)
    show_all_box()
# print(image_list[0:2],'\n',label_file_name)
