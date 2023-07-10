from flask import Flask, render_template, Response, request
from werkzeug.utils import secure_filename
import datetime, time
import cv2, os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/capture', methods=['POST'])
def capture():
    print("here")
    file = request.files['file']
    if file:
        now = str(datetime.datetime.now()).replace(" ","")
        print(file.filename.split('.'))
        file.save('photos/' + f'{str(file.filename).replace(" ","_").split(".")[0]}_{str(now).replace(":","")}.{file.filename.split(".")[1]}')
        return 'Arquivo salvo com sucesso!'
    else:
        return 'Nenhum arquivo foi enviado.'
    

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

