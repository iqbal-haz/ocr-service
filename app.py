from base64 import b64encode
from dotenv import load_dotenv
from flask import Flask, render_template, flash, request, url_for, redirect, jsonify
from io import BytesIO
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
from werkzeug.utils import secure_filename
import urllib.request
import os

load_dotenv()

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

ocr = PaddleOCR(use_angle_cls=True, lang='en')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['POST'])
def upload_img():

    if 'image' not in request.files:
        print('No image')
        return redirect(request.url)
        
    image = request.files['image']
    if image.filename == '':
        print('No image selected')
        return redirect(request.url)

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(img_path)

        image_pil = Image.open(image)

        # Kode OCR disini
        result = ocr.ocr(img_path)
        txts = [line[1][0] for line in result]
        fulltxt = ' '.join(txts)

        # context = jsonify(img_path=img_path, fulltxt=fulltxt)
        # print(context)

        context = {'img_path': img_path, 'fulltxt': fulltxt}
        print(context)

        return context

if __name__ == "__main__":
    print("APP RUNNING...")
    app.run()