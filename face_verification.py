import cv2

def face_verification(img_path):
    # Get user supplied values
    cascPath = "facial.xml"
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)
    # Read the image
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    if len(faces) == 1:
        print(f"Found {len(faces)} faces!")
        return True
    else:
        print(faces)
        print("Either 0 or more than 1 face detected!!")
        return False
    # Draw a rectangle around the faces
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)