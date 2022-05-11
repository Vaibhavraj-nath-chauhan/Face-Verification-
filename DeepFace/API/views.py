# import the necessary packages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import numpy as np
import urllib
import json
import cv2
from deepface import DeepFace


@csrf_exempt
def detect(request):
    # initialize the data dictionary to be returned by the request
    data = {"success": False}
    # check to see if this is a post request
    if request.method == "POST":
        # check to see if an image was uploaded
        if request.FILES.get("image", None) is not None:
            # grab the uploaded image
            image = _grab_image(stream=request.FILES["image"])
            image1 = _grab_image(stream=request.FILES['image1'])
            result = _get_data(image, image1)
            result["Confidance"] = ((2 - result["distance"]) ** 2 - 1) / 3
            # otherwise, assume that a URL was passed in
        else:
            data["Message"] = "Accept only system image"
            return JsonResponse(data)

        data = result
    # return a JSON response
    return JsonResponse(data)


def _grab_image(stream=None):
    if stream is not None:
        data = stream.read()
        # convert the image to a NumPy array and then read it into
        # OpenCV format
        image = np.asarray(bytearray(data), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    else:
        return {"Success": False, "Error":"Accept only system images"}

        # return the image
    return image


def _get_data(img1, img2):
    return DeepFace.verify(img1_path=img1, img2_path=img2, model_name="Dlib", distance_metric="cosine",
                           detector_backend="mtcnn")