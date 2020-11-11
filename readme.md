python3 -m venv python3-virtualenv  
source python3-virtualenv/bin/activate

cd ration-ocr-django  
pip3 install -r requirements.txt

cd mysite  
python3 manage.py runserver 0.0.0.0:8000 &