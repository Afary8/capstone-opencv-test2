import cv2

# Create the marker and save it as an image.
dictionary = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_4X4_50
)

marker = cv2.aruco.generateImageMarker(dictionary, 0, 500)

marker = cv2.copyMakeBorder(
    marker, 80, 80, 80, 80,
    cv2.BORDER_CONSTANT, value=255
)

cv2.imwrite("marker.png", marker)
print("Marker saved as marker.png")

# Open the webcam and look for markers.
detector = cv2.aruco.ArucoDetector(dictionary)
camera = cv2.VideoCapture(0)

try:
    if not camera.isOpened():
        raise RuntimeError("Check your camera permissions.")

    while True:
        success, frame = camera.read()
        if not success:
            break

        corners, ids, _ = detector.detectMarkers(frame)

        if ids is not None:
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        cv2.imshow("Marker test - press Q to stop", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    camera.release()
    cv2.destroyAllWindows()