from dotenv import load_dotenv
from flask import Flask, request, redirect, jsonify
from paddleocr import PaddleOCR
from PIL import Image
from tempfile import TemporaryDirectory
from werkzeug.utils import secure_filename
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

ocr = PaddleOCR(use_angle_cls=True, lang='en')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['POST'])
def upload_img():
    global UPLOAD_FOLDER
    UPLOAD_FOLDER = TemporaryDirectory()
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    if 'image' not in request.files:
        print(request.files)
        print('No image')
        return redirect(request.url)
        
    image = request.files['image']
    if image.filename == '':
        print('No image selected')
        return redirect(request.url)

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        img_path = os.path.join(app.config['UPLOAD_FOLDER'].name, filename)
        image.save(img_path)

        # Kode OCR disini
        result = ocr.ocr(img_path)
        txts = [line[1][0] for line in result]
        fulltxt = ' '.join(txts)

        context = jsonify(img_path=img_path, fulltxt=fulltxt)
        print(context.data)

        UPLOAD_FOLDER.cleanup()
        app.config['UPLOAD_FOLDER'].cleanup()

        return context

    UPLOAD_FOLDER.cleanup()
    app.config['UPLOAD_FOLDER'].cleanup()

if __name__ == "__main__":
    app.run()