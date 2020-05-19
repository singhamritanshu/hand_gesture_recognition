#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 09:20:17 2019

@author: amritanshusingh
"""
import cv2

import numpy as np 

import math

hand = cv2.imread('hand.png',0)

ret, the = cv2.threshold(hand, 70, 250, cv2.THRESH_BINARY)

_,contours,_ = cv2.findContours(the.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull= [cv2.convexHull(c)for c in contours]

final = cv2.drawContours(hand, hull, -1, (255, 0, 0))

cv2.imshow('Original Image', hand)

cv2.imshow('Thresh', the)

cv2.imshow('Convex Hull', final)

cv2.waitKey(0)

cv2.destroyAllWindows()

