import base64
import io
import PIL
def detect_faces_uri(uri):
    """Detects faces in the file located in Google Cloud Storage or the web."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

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
        return landmarks
    #     mouthleftx = landmarks[10].position.x
    #     mouthtop = landmarks[8].position.y
    #     mouthrightx = landmarks[11].position.x
    #     mouthbottom = landmarks[9].position.y
    #
    # im = Image.open('/selfie.png')
    # print(round(mouthleftx))
    # print(round(mouthtop))
    # print(round(mouthrightx))
    # print(round(mouthbottom))
    # crop_rectangle = (round(mouthleftx) - round(mouthleftx * .05), round(mouthtop) - round(mouthtop*.05), round(mouthrightx) + round(mouthrightx *.05), round(mouthbottom) + round(mouthbottom * .05))
    # cropped_im = im.crop(crop_rectangle)
    # cropped_im.save("/Users/Raveen/Desktop/echacks/data_processed/mouth/drunk/drunkmouth-%d.png")

def hello_world(request):
    request_json = request.get_json()
 #   imgdata = base64.b64decode(request_json['uri'])
    detect_faces_uri(request_json['uri'])


