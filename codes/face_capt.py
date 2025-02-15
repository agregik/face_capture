import cv2


def face_capture():
    cascade_path = 'face_capture/haarcascade_frontalface_default.xml'
    
    clf = cv2.CascadeClassifier(cascade_path)
    camera = cv2.VideoCapture('face_capture/filter/girl.mp4')
    
    while True:
        _, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = clf.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)
            
        cv2.imshow('Faces', frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
        
    camera.release()
    cv2.destroyAllWindows()


def main():
    face_capture()
    
    
if __name__ == '__main__':
    main()



# import threading
# import cv2
# from deepface import DeepFace

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# counter = 0

# reference_img = cv2.imread("face_capture/me.jpg")  # use your own image here

# face_match = False


# def check_face(frame):
#     global face_match
#     try:
#         if DeepFace.verify(frame, reference_img.copy())['verified']:
#             face_match = True
#         else:
#             face_match = False
#     except ValueError:
#         face_match = False


# while True:
#     ret, frame = cap.read()

#     if ret:
#         if counter % 30 == 0:
#             try:
#                 threading.Thread(target=check_face, args=(frame.copy(),)).start()
#             except ValueError:
#                 pass
#         counter += 1
#         if face_match:
#             cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
#         else:
#             cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

#         cv2.imshow('video', frame)

#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break

# cv2.destroyAllWindows()
    

    # from keras_preprocessing.image import load_img
