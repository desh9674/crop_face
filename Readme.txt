Ok, First of All I could create a Virtual Env for this but i dont't want to for tedious reasons.
This is a one file project, which can be built upon more, but the again am not an HTML fan. I hate JAVA.


To get this working, you need
Flask, cv2, PIL and Numpy installed.


I kow Machine Learning, almost all of it(how to use it), but i did get any opportunity to apply it somewhere,
Untill Now-

Now to what this app is:

Simply put, it is a webiste where you can upload any image and when it returns the first face it detecs in the image,

(It uses cv2 face detection machine learning model for detection) Its already trained.
It also saves uploaded image and cropped image in dolders, database is yet to be linked
am going to use sqlite


!!!Possibilities are many, just replace face to detect anything else, but it will need a trained model first.

I just took the model into application. No one in entire world has done anything like this, I have looked.
this is my Unique project.

Code for multiple images and multiple faces in one image is in works. 

TO run this program, follow the steps.


1) Copy all the project( entire repo) to any folder
 
2) Now open cmd and change current directorry to project folder
path -- cd C:\Users\dhira\Desktop\mywork\Virtual Envs projects\Crop_faces\

3) Now export app by typing,
set FLAS_APP=test5.py


4) Now simple type- flask run



5)THAts it, now open localhost on your browser and you should see the site ready.
* Serving Flask app "test5.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)



I would put this up on Internet if someone pays for the domain or hosting services.