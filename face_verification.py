import cv2
import pytesseract

# Get user supplied values
cascPath = "facial.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread('/home/sukesh/Pictures/istockphoto-1211345565-612x612.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
)
if len(faces) == 1:
    print("Found {0} faces!".format(len(faces)))
else:
    print("Please Upload The Correct Document!!")

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

