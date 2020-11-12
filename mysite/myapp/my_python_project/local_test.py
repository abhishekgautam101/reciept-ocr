import cv2
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def houghTransform(image):
	#image = cv2.imread('1.jpg')

	result = image.copy()
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

	# Remove horizontal lines
	horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40,1))
	remove_horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
	cnts = cv2.findContours(remove_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if len(cnts) == 2 else cnts[1]
	for c in cnts:
	    cv2.drawContours(result, [c], -1, (255,255,255), 1)

	# Remove vertical lines
	vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,40))
	remove_vertical = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
	cnts = cv2.findContours(remove_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if len(cnts) == 2 else cnts[1]
	for c in cnts:
	    cv2.drawContours(result, [c], -1, (255,255,255), 1)

	#cv2.imshow('thresh', thresh)
	#cv2.imshow('result', result)
	#cv2.imwrite('result.png', result)

	custom_psm_config = r'--psm 6 --oem 2'
	return pytesseract.image_to_string(result, lang='eng+hin+san', config=custom_psm_config)



import os
from datetime import datetime
#USERNAME
username = '/root/'
output_folder = username+'abhi_output_txt_files'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

folder = username + 'NOT_DONE_FILES'
for filename in os.listdir(folder):

	start=datetime.now()

	img = cv2.imread(os.path.join(folder,filename))
	if img is not None:
		ocr_res = houghTransform(image)

		f= open(output_folder+'/'+filename+".txt","w+")
		f.write(ocr_res)
		f.close()

		print(datetime.now()-start)
		print('\n')