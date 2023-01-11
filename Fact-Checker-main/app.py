from flask import Flask, render_template, jsonify, request
from main import main
from flask_cors import CORS
from PIL import Image
#sys.path.append('Fact-Checker-main')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict" ,methods=['POST', 'GET'])
def predict():
    imagefile = request.files.get("imagefile", '')
    print('poop',imagefile, 'peep')
    #img = Image.open(image)
    response = main(imagefile)
    print(response)


if __name__ == '__main__':
    app.run(debug=True)