#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from PIL import Image
import time


def getf1(input):
    img = Image.open(input)
    res = (img.getpixel((0,0)))
    return res

def cutjpg(injpg,outjpg,m,n,q,p):
    img = Image.open(injpg)
    #print(img.size)
    cropped = img.crop((m,n,q,p))  # (left, upper, right, lower)
    cropped.save(outjpg)

# def cutjpg(injpg,m,n,q,p):
#     img = Image.open(injpg)
#     #print(img.size)
#     cropped = img.crop((m,n,q,p))
#     return cropped

def highlight(input,r1,r2,g1,g2,b1,b2):
    img = Image.open(input)
    coor_arr = []
    i = 1
    j = 1
    width = img.size[0]
    height = img.size[1]
    for i in range(0, width):  # 遍历所有长度的点
        for j in range(0, height):  # 遍历所有宽度的点
            data = (img.getpixel((i, j)))
            if (data[0] <= r2 and data[1] <= g2 and data[2] <= b2 and data[0] >= r1 and data[1] >= g1 and data[2] >= b1):
                coor_arr.append((i,j))
    # img = img.convert("RGB")
    # img.save(output)
    return coor_arr

def rgb (picture,l,u,r,d):
    arr = []
    img = Image.open(picture)
    for i in range(l, r):  # 遍历所有长度的点
        for j in range(u, d):  # 遍历所有宽度的点
            data = (img.getpixel((i, j)))  # 打印该图片的所有点
            arr.append(data)
            #print(data)  # 打印每个像素点的颜色RGBA的值(r,g,b,alpha)
    return arr

def tag_arr(input):
    arr = []
    img = Image.open(input)
    for i in range(0,img.size[0]-1):
        for j in range(0,img.size[1]-1):
            data = (img.getpixel((i, j)))
            arr.append(data)
    return arr

def get_to_selec(input,tage_arr,x):
    arr = []
    img = Image.open(input)
    for j in range(0, img.size[1]-1):
        data = (img.getpixel((x, j)))
        if data[0] == tage_arr[0][0] and data[1] == tage_arr[0][1] and data[2] == tage_arr[0][2]:
            arr.append((x,j))
    return arr

def get_to_selechb(input,tage_arr):
    arr = []
    img = Image.open(input)
    for i in range(0, img.size[0]-1):
        for j in range(0, img.size[1]-1):
            data = (img.getpixel((i, j)))
            if data[0] == tage_arr[0][0] and data[1] == tage_arr[0][1] and data[2] == tage_arr[0][2]:
                arr.append((i,j))
    return arr

def get_clock_coor(input,to_slec_arr,a,tag):
    img = Image.open(input)
    tagimg = Image.open(tag)
    for i in to_slec_arr:
        arr = []
        cun = 0
        for x in range(i[0],i[0]+tagimg.size[0]-1):
            for y in range(i[1],i[1]+tagimg.size[1]-1):
                data = (img.getpixel((x,y)))
                arr.append(data)
        for n in range(0,len(a)):
            d1 = abs(a[n][0] - arr[n][0])
            d2 = abs(a[n][1] - arr[n][1])
            d3 = abs(a[n][2] - arr[n][2])
            if d1 < 5 and d2 < 5 and d3 < 5:
                cun = cun + 1
            v = cun/len(a)
            if (v > 0.99):
                return i
            else:
                pass

def clock_hb(input,tag):
    tag = tag
    #x = 252
    tar_a = tag_arr(tag)
    to_selec_coor = get_to_selechb(input,tar_a)
    clock_coor = get_clock_coor(input, to_selec_coor, tar_a, tag)
    return clock_coor

def clock_gx(input,tag):
    tag = tag
    x = 160
    tar_a = tag_arr(tag)
    to_selec_coor = get_to_selec(input,tar_a,x)
    clock_coor = get_clock_coor(input, to_selec_coor, tar_a, tag)
    return clock_coor

#def money(input):

def shibie(input):
    cmd = 'tesseract.exe --psm 9 --dpi 70 '+input+' stdout'
    print (cmd)
    res = os.popen(cmd).readlines()
    return (res[0].strip().strip('.'))
    # res = os.popen(cmd).read()
    # return res

def get_money(input,money):
    cutjpg(input, money, 152,435,456,531)
    time.sleep(0.1)
    nk = shibie(money)
    return nk
# input1 = 'c://Users//28618//Desktop//screens1hot.png'
# input2 = 'c://Users//28618//Desktop//screenshosst.png'
# n = clock_gx(input2)
# print(n)
# m = clock_gx(input2)
# print(m)
# coor = clock_hb('liebiao.png','hongbao.png')
# print(coor[0])
# input3 = 'c://Users//28618//Desktop//moneyt.png'
#
# nk = get_money(input3)
# print(nk)


