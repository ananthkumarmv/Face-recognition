from PIL import Image, ImageDraw
import face_recognition


image = face_recognition.load_image_file("people.jpg")

# Finds all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

# Loading the image into a Python Image Library object so that we can draw on top of it and display it
pil_image = Image.fromarray(image)

# Creates a PIL drawing object to be able to draw lines later
d = ImageDraw.Draw(pil_image, 'RGBA')

for face_landmarks in face_landmarks_list:
    # The face landmark detection model returns these features:
    #  - chin, left_eyebrow, right_eyebrow, nose_bridge, nose_tip, left_eye, right_eye, top_lip, bottom_lip

    # Draws a line over the eyebrows
    d.line(face_landmarks["left_eyebrow"], fill=(128, 0, 128, 100), width=3)
    d.line(face_landmarks["right_eyebrow"], fill=(128, 0, 128, 100), width=3)



    # Draws over the lips
    d.polygon(face_landmarks["top_lip"], fill=(128, 0, 128, 100))
    d.polygon(face_landmarks["bottom_lip"], fill=(128, 0, 128, 100))



pil_image.show()
