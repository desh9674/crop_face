import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


import os,shutil,re, cv2
import numpy as np
from PIL import Image


UPLOAD_FOLDER = 'Captures'
cropped_folder = "Cropped"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = 'something_secret_key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img = cv2.imread(UPLOAD_FOLDER+"\\"+filename)
            img = cv2.resize(img,(1080,720))
            face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            faceRect = face_cascade.detectMultiScale2(img,1.3, 5)
            if faceRect != ((),()):
              for (x,y,w,h) in faceRect[0]:      # syntx
                face = cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),3)  # draw rectancgle 
                #faces.append(face)
                crop_img = img[y:y+h, x:x+w].copy()
                file1 = cv2.imwrite(cropped_folder+"\\"+filename,crop_img)           
            #file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))            
                return redirect(url_for('uploaded_file',filename=filename))
            else:
                flash("No faces in given Image")
                return redirect(request.url)
    return render_template('index1.html')

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(cropped_folder,
                               filename)

#if __name__ == '__main__':
#    app.run(host= '0.0.0.0', port=5000, debug=False)
