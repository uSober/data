import io
from PIL import Image
leftx = 0
rightx = 100
bottom = 0
top = 100
def detect_faces(path):
    landmarks = 0
    """Detects faces in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')
    for face in faces:
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])
        print('face bounds: {}'.format(','.join(vertices)))
        landmarks = face.landmarks
        print(landmarks)
        leftx = landmarks[10].position.x
        top = landmarks[8].position.y
        rightx = landmarks[11].position.x
        bottom = landmarks[9].position.y

    im = Image.open('/Users/Raveen/Desktop/echacks/data_processed/drunk/pic%d.png' % i)
    print(round(leftx))
    print(round(top))
    print(round(rightx))
    print(round(bottom))
    crop_rectangle = (round(leftx) - round(leftx * .05), round(top) - round(top*.05), round(rightx) + round(rightx *.05), round(bottom) + round(bottom * .05))
    cropped_im = im.crop(crop_rectangle)
    cropped_im.save("/Users/Raveen/Desktop/echacks/data_processed/mouth/drunk/drunkmouth-%d.png" % i)


for i in range(1,80):
    detect_faces('/Users/Raveen/Desktop/echacks/data_processed/drunk/pic%d.png' %i)