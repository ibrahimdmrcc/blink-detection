from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
import argparse
import imutils
import dlib
import cv2
import pyautogui
import time
import webbrowser

def eye_aspect_ratio(eye):												# ORANIN HESAPLANDIĞI FONKSİYON
																		# FUNCTION WHICH CALCULATING EYE RATE
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])
	C = dist.euclidean(eye[0], eye[3])

	ear = (A + B) / (2.0 * C)

	return ear


def healt():                                                       #bu mmetod göz sağlığı için yazılan modda çalışmakta.
																   #FUNCTION FOR EYE HEALT MODE.
	ap = argparse.ArgumentParser()
	ap.add_argument("-p", "--shape-predictor", required=True,
					help="path to facial landmark predictor")

	args = vars(ap.parse_args())

	EYE_AR_THRESH = 0.22
	EYE_AR_CONSEC_FRAMES = 3
	EYE_AR_CONSEC_FRAMES1= 30

	COUNTER = 0
	COUNTER2=0
	TOTAL = 0
	QUIT = 0

	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor(args["shape_predictor"])

	(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
	(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]



	vs = VideoStream(src=0).start()

	time.sleep(1.0)

	while True:


		CLOSE = 0
		QUIT = 0
		frame = vs.read()
		frame = imutils.resize(frame, width=500)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


		rects = detector(gray, 0)

		for rect in rects:

			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)

			leftEye = shape[lStart:lEnd]
			rightEye = shape[rStart:rEnd]
			leftEAR = eye_aspect_ratio(leftEye)
			rightEAR = eye_aspect_ratio(rightEye)


			ear = (leftEAR + rightEAR) / 2.0

			leftEyeHull = cv2.convexHull(leftEye)
			rightEyeHull = cv2.convexHull(rightEye)
			cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
			cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

			if ear < EYE_AR_THRESH:
				COUNTER += 1
				CLOSE +=1
				if COUNTER >= EYE_AR_CONSEC_FRAMES1:	#BU IF BLOGU GOZLERI 3 SANIYE KAPALI TUTARAK PROGRAMDAN ÇIKMAK ICIN
					if not QUIT:						# THIS IF BLOCK FOR CLOSE THE PROGRAM
						QUIT=1

			else:

				QUIT = 0
				if COUNTER >= EYE_AR_CONSEC_FRAMES:
					TOTAL += 1
					COUNTER = 0
					COUNTER2=0

#################################################################################### BU BÖLÜMDE 3 SANİYELİĞİNE UYARI PENCERESİ AÇILIYOR.
			if ear > 0.25:															# CREATING A WARNING WİNDOW FOR 3 SECONDS
				COUNTER2 += 1

			if COUNTER2 >= 200:
				imgs =cv2.imread("img.jpeg")
				cv2.imshow('WARNING',imgs)

				cv2.waitKey(2000)
				cv2.destroyAllWindows()
				COUNTER2 = 0

####################################################################################
		# show the frame
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

		if QUIT:
			break

	cv2.destroyAllWindows()
	vs.stop()

def pdf_video_set(l,r):                                               #bu fonksiyon pdf, youtube video kontrol etme ve set mode açıldığında çalışmakta.
																	  #FUNCTION FOR PDF, VIDEO CONTROLLER AND SET MODE
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--shape-predictor", required=True,
                    help="path to facial landmark predictor")

    args = vars(ap.parse_args())

    EYE_AR_THRESH = 0.2
    EYE_AR_CONSEC_FRAMES1 = 20

    leftCOUNTER = 0
    rightCOUNTER = 0
    COUNTER = 0
    leftTOTAL = 0
    rightTOTAL = 0
    TOTAL = 0
    QUIT = 0


    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(args["shape_predictor"])

    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


    vs = VideoStream(src=0).start()

    time.sleep(1.0)

    while True:
        CLOSE = 0
        QUIT = 0
        frame = vs.read()
        frame = imutils.resize(frame, width=550, height=700)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        rects = detector(gray, 0)

        for rect in rects:

            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)

            ear = (leftEAR + rightEAR) / 2.0

            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)			#SAG VE SOL GOZU CIZME
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)			#DRAWING LEFT AND RIGHT EYE

#########################################
            if ear < EYE_AR_THRESH:
                CLOSE+=1
                COUNTER += 1
                if COUNTER >= EYE_AR_CONSEC_FRAMES1:			#BU IF BLOGU GOZLERI 3 SANIYE KAPALI TUTARAK PROGRAMDAN ÇIKMAK ICIN
                    if not QUIT:								# THIS IF BLOCK FOR CLOSE THE PROGRAM
                        QUIT=1

            else:
                QUIT = 0
                COUNTER = 0
##############################
            if leftEAR < 0.20 and rightEAR < 0.20:
                pass
            elif leftEAR > 0.20 and rightEAR < 0.20:
                rightCOUNTER += 1
            elif leftEAR < 0.20 and rightEAR > 0.20:
                leftCOUNTER += 1

            else:
                if leftCOUNTER > 1:
                    leftTOTAL += 1
                    pyautogui.press(l)


                elif rightCOUNTER > 1:
                    rightTOTAL += 1
                    pyautogui.press(r)

                leftCOUNTER = 0
                rightCOUNTER = 0


        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF


        if QUIT:

            break
    cv2.destroyAllWindows()
    vs.stop()

def dino():                                                              # bu fonksiyon dino game modu açıldığında çalışmakta.
																		 # FUNCTION FOR DINO GAME MODE

	url = "https://elgoog.im/t-rex/"
	webbrowser.open_new(url)											#OPENING DINO GAME ON WEB BROWSER

	ap = argparse.ArgumentParser()
	ap.add_argument("-p", "--shape-predictor", required=True,
					help="path to facial landmark predictor")

	args = vars(ap.parse_args())

	EYE_AR_THRESH = 0.20
	EYE_AR_CONSEC_FRAMES = 3
	EYE_AR_CONSEC_FRAMES1= 20

	COUNTER = 0
	TOTAL = 0
	QUIT = 0

	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor(args["shape_predictor"])

	(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
	(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

	vs = VideoStream(src=0).start()

	while True:

		CLOSE = 0
		QUIT = 0
		frame = vs.read()
		frame = imutils.resize(frame, width=500)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		rects = detector(gray, 0)

		for rect in rects:

			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)

			leftEye = shape[lStart:lEnd]
			rightEye = shape[rStart:rEnd]
			leftEAR = eye_aspect_ratio(leftEye)
			rightEAR = eye_aspect_ratio(rightEye)

			ear = (leftEAR + rightEAR) / 2.0

			leftEyeHull = cv2.convexHull(leftEye)
			rightEyeHull = cv2.convexHull(rightEye)
			cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)			#DRAWING LEFT AND RIGHT EYE
			cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)			#SAG VE SOL GOZU CIZME

			if ear < EYE_AR_THRESH:
				COUNTER += 1
				CLOSE +=1
				if COUNTER >= EYE_AR_CONSEC_FRAMES1:
					if not QUIT:
						QUIT=1

			else:
				QUIT = 0
				if COUNTER >= EYE_AR_CONSEC_FRAMES:
					TOTAL += 1
					pyautogui.press("space")

				COUNTER = 0


		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

		if QUIT:
			pyautogui.hotkey("alt","f4")
			time.sleep(1)
			pyautogui.press("enter")
			break
	cv2.destroyAllWindows()
	vs.stop()