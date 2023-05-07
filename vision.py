# import the opencv library
import cv2
import numpy
#import requests
#import json
#from flask import jsonify
from pygame import *
import winsound

counter = 0
minA = 0
maxA = 0
errorMar = 0
safeRadius = 0
obsticles = []

def th(*args):
	global counter
	counter = args[0]

def minArea(*args):
	global minA
	minA = args[0]*100

def maxArea(*args):
	global maxA
	maxA = args[0]*100

def errorMargin(*args):
	global errorMar
	errorMar = args[0]/10

def changeSaftey(*args):
	global safeRadius
	safeRadius = int(args[0]*1.3)

def run():

	mixer.init()

	global counter 
	global minA 
	global maxA
	global errorMar 
	global safeRadius 
	global obsticles

	#define a video capture object
	vid = cv2.VideoCapture(1, cv2.CAP_DSHOW)

	#PARAMETERS FOR DIFFERENT LIGHTING CONDITIONS
	cv2.namedWindow("Parameters")
	cv2.resizeWindow("Parameters", 640, 240)
	cv2.createTrackbar("Threshold", "Parameters", 0, 255, th)
	cv2.setTrackbarPos("Threshold", "Parameters", 175)
	cv2.createTrackbar("minArea", "Parameters", 0, 300, minArea)
	cv2.setTrackbarPos("minArea", "Parameters", 7)
	cv2.createTrackbar("maxArea", "Parameters", 0, 300, maxArea)
	cv2.setTrackbarPos("maxArea", "Parameters", 300)
	cv2.createTrackbar("marginOfError", "Parameters", 0, 10, errorMargin)
	cv2.setTrackbarPos("marginOfError", "Parameters", 1)
	cv2.createTrackbar("safe radius", "Parameters", 1, 100, changeSaftey)
	cv2.setTrackbarPos("safe radius", "Parameters", 60)

	sound = mixer.Sound("beep-02.mp3")
	voice = mixer.Channel(5)

	while(True):

		#Read frame from webcam
		ret, frame = vid.read()

		#blur to improve accuracy
		blur = cv2.GaussianBlur(frame, (7,7), 0)

		#Convert to grayscale and use binary thresholding to isolate shapes
		#THIS IS FOR SHAPE DETECTION
		converted = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		ret, thresh = cv2.threshold(converted, counter, 255, cv2.THRESH_BINARY_INV)
		contours, heierchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		#converts the image to hue saturation value colour sustem cuz easier to work with
		# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		# lower_bound = numpy.array([0,0,0])
		# upper_bound = numpy.array([180,255,255])

		# mask = cv2.inRange(hsv, lower_bound, upper_bound)

		#This list stores two coordinates to create a vector for the direction the robot is facing
		#triangle for direction, square for other coordinate
		points = [0, 0]

		obsticles = []
				
		for i, contour in enumerate(contours):
			#continue here because it is detecting entire screen
			if i == 0:
				continue
			epsilon = errorMar*cv2.arcLength(contour, True)
			approx = cv2.approxPolyDP(contour, epsilon, True)
			
			x, y, w, h = cv2.boundingRect(approx)
			middleX = int(x - w/3)
			middleY = int(y - h/1.5)

			coords = (middleX, middleY)
			colour = (0,0,0)

			if maxA > w * h > minA and x!= 0 and y != 0:
				cv2.rectangle(frame, (int(x), int(y)), (int(x+w), int(y+h)), (0,0,255), thickness=10, lineType=cv2.LINE_8)
				cv2.circle(frame, (int(x)+int(w/2), int(y)+int(h/2)), 10, (0, 255, 0), thickness=5, lineType = cv2.LINE_AA)
				
				#use to get center point of robot
				if len(approx) == 4:
					print(approx[0][0])
					if points[0] == 0:
						points[0] = (int(x)+int(w/2), int(y)+int(h/2))
					elif points[1] == 0:
						points[1] = (int(x)+int(w/2), int(y)+int(h/2))
				#tip
				elif len(approx) == 3:
					obsticles.append((int(x)+int(w/2), int(y)+int(h/2), h//2))
					#points[0] = (int(x)+int(w/2), int(y)+int(h/2))
			
		if (points[0] and points[1]):
			cv2.line(frame, points[0], points[1], (255, 0, 0), thickness=3)
			midPointX = (points[0][0]+points[1][0])//2
			midPointY = (points[0][1]+points[1][1])//2
			# cv2.circle(frame, (midPointX, midPointY), 10, (0, 255, 0), thickness=5, lineType = cv2.LINE_AA)
			cv2.circle(frame, (midPointX, midPointY), safeRadius, (0, 255, 0), thickness=5, lineType = cv2.LINE_AA)
			# print(len(obsticles))
			# lastDistSqr = 1000
			# minDistSqr = 12345
			# freq = 800 
			# margin = 100
			# dur=50
			for o in obsticles:
				distSqr= (midPointX-int(o[0]))**2 + (midPointY-int(o[1]))**2 
				safeDistSqr = (safeRadius + o[2])**2
				if distSqr  < safeDistSqr:
					if distSqr  < safeDistSqr:
						cv2.circle(frame, (midPointX, midPointY), safeRadius, (0, 0, 255), thickness=5, lineType = cv2.LINE_AA)
						if not voice.get_busy():
							voice.play(sound)
			# print(round(minDistSqr,2))
					
			# requests.post("http://127.0.0.1:8000/base", json = {"base" : {points[1][0] : points[1][1]}, "tip" : {points[0][0] : points[0][1]}})
			#jsonify('{"base" : {"x" : points[1][0], "y" : points[1][1]}, "tip" : {"x" : points[0][0], "y" : points[0][1]}}')
			#requests.post("http://127.0.0.1:8000/base", json = {"base" : {"x" : points[1][0], "y" : points[1][1]}, "tip" : {"x" : points[0][0], "y" : points[0][1]}})
	
		cv2.imshow('frame', frame)
		cv2.imshow('thresh', thresh)
		
		k = cv2.waitKey(1)
		if k == ord('q'):
			break

	#Release video object
	vid.release()
	#Destroy Windows
	cv2.destroyAllWindows()