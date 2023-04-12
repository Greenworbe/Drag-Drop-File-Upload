from flask import Flask, render_template, jsonify, request
from main import main
from werkzeug.utils import secure_filename
import os
import numpy as np
import cv2
from werkzeug.datastructures import  FileStorage
#from flask_cors import CORS
from PIL import Image
#sys.path.append('Fact-Checker-main')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict" ,methods=['POST', 'GET'])
def predict():
    #gets image file name from request
    imagefile = request.files['imagefile'].read()
    #converts file object to bytes
    imgbytes = np.fromstring(imagefile, np.uint8)
    print(imgbytes.shape)
    #converts bytes to image
    img = cv2.imdecode(imgbytes, cv2.IMREAD_COLOR)
    print('poop', img.shape, 'peep')

    #gets text from ocr, response = the text
    response = main(img)
    #this response should be outputted somewhere in the site
    print(response)


if __name__ == '__main__':
    app.run(debug=True)