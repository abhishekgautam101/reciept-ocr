from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
	# I am importing the 'houghTransform' function defined in 'test.py' file inside 'mysite/myapp/my_python_project' folder.
from .my_python_project.test import houghTransform


@csrf_exempt
def index(request):
	if request.method == 'POST':
			# Accepting POST request from the user
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)

		    # I am expecting a key,value pair where key is 'image' and value is base64 string.
		base64string = body['image']

			# converting the base 64 string into an image
		import base64
		from PIL import Image
		from io import BytesIO
		import numpy as np
		im = Image.open(BytesIO(base64.b64decode(base64string)))
		npImage = np.array(im)
		#im.save('image1.jpg', 'JPG')

			# I am passing image (data in HTTP request) to my imported function and storing result in 'result' variable. 
		result = houghTransform(npImage)

		# 	# Structuring the response into a json
		# result = []

		# resDict = {
		# 'question': question,
		# 'answers': answers
		# }

		# result.append(resDict)

		# json_result = json.dumps({"result":result})

		    # Sending HTTP response back to the user
		return HttpResponse(result)
	else:
		return HttpResponse("Error! Not a valid request.")