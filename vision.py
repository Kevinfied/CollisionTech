# import the opencv library
import cv2

# define a video capture object
vid = cv2.VideoCapture(0)

counter = 192

while(True):
	
	# Capture the video frame
	# by frame
	ret, frame = vid.read()
	# Display the resulting frame
	
	blur = cv2.GaussianBlur(frame, (5,5), 0)
	converted = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
	# ret, thresh = cv2.threshold(converted, counter, 255, cv2.THRESH_BINARY_INV)
	ret, thresh = cv2.threshold(converted, counter, 255, cv2.THRESH_BINARY_INV)

	contours, heierchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for i, contour in enumerate(contours):
		if i == 0:
			continue
		epsilon = 0.01*cv2.arcLength(contour, True)
		approx = cv2.approxPolyDP(contour, epsilon, True)
		# cv2.drawContours(frame,contour, 0, (255, 0, 0), 4)
		
		x, y, w, h = cv2.boundingRect(approx)
		middleX = int(x - w/3)
		middleY = int(y - h/1.5)

		coords = (middleX, middleY)
		colour = (0,0,0)
		font = cv2.FONT_HERSHEY_DUPLEX

		if len(approx) == 4:
			# cv2.putText(frame, "RECTANGLE", coords, font, 1, colour, 1)
			if (w*h) >20000 and x!= 0 and y != 0:
				c = frame.copy()
				cv2.rectangle(c, (int(x), int(y)), (int(x+w), int(y+h)), (0,0,255), thickness=3, lineType=cv2.LINE_8)
				print(x, y)
 
	cv2.imshow('frame', frame)
	cv2.imshow('thresh', thresh)
	
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	if cv2.waitKey(1) & 0xFF == ord('n'):
		counter-=1
	if cv2.waitKey(1) & 0xFF == ord('m'):
		counter+=1
	#qqprint(counter)

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
