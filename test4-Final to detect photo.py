

# find all images in database and put their paths in a list
import os,shutil,re, cv2
import numpy as np
from PIL import Image


def imags(Path='\\'):
 abspathfiles = []
 myregx = re.compile(r'''^(.*?)          #beforepart anything
                    (\.)                #escape . caracter
                    ((jpg)|(png)|JPEG|jpeg|PNG)$      #extension
                    ''', re.VERBOSE)


 for folderdir, subfolderdir, fileNameList in os.walk(Path): #Path to project
    #print(fileNameList)
    
    for fileName in fileNameList:
        mo = myregx.search(fileName)

        if mo==None:
            #print("No images found")
            continue
        else:
            filename = mo.group(1)
            extension= mo.group(3)
            file = filename+extension
            absWrkingdir = folderdir+'\\'+ fileName     #get absolute path of those files
            abspath =absWrkingdir                       # IF REQUIRED os.path.join(absWrkingdir, fileANY)
            abspathfiles.append(abspath)     ## just the list of files scanned
        
    if abspathfiles==[]:
        print("No images found")
    else:
        print(abspathfiles)
        return(abspathfiles)


#imags("C:\\Users\\dhira\\Desktop\\mywork\\Virtual Envs projects\\faces")


def preprop(imagpathlist):
    n=0
    faces = []
    for abspath in imagpathlist:
        img = cv2.imread(abspath)  # reading the image

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  ## grey image, use if required
        img = cv2.resize(img,(1080,720))  #### This gives the best result, but change all you want or Keep the resolution as it is

        
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   # path to file containing facial features
        # Select one of the haarcascade files:
        #   haarcascade_frontalface_alt.xml  <-- Best one?
        #   haarcascade_frontalface_alt2.xml
        #   haarcascade_frontalface_alt_tree.xml
        #   haarcascade_frontalface_default.xml
        #   haarcascade_profileface.xml        
        #   there are many more files(pre-trained models from Cv2) for various features of face, eyes, noses,etc, located at, Install more as needed
        #   C:\Users\dhira\Desktop\mywork\ML\Datas\cascades  ###  features usually located here but, giving path does NOT work
        #   for some reason they do not work directly then simply copy and paste them in current folder
        
        faceRect = face_cascade.detectMultiScale2(img,1.3, 5)  # creates a face rectangle on image, scaling parameters are complex, dosent matter keep it as it is,
        
        #add bracket to see full syntax,  It has already detected face in faceRect, now is only showing part on the image
        #print(faceRect)
        #Show face on image
        
       
        for (x,y,w,h) in faceRect[0]:      # syntx
            face = cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),3)  # draw rectancgle
            faces.append(face)
            crop_img = img[y:y+h, x:x+w].copy()
            #cv2.imshow('Img_name', faces) ## Shows face rectangle on actual image
            cv2.imshow('Img_name', crop_img) ##Shows cropped face image
            cv2.waitKey(0) # 0 is Esc key
            cv2.destroyAllWindows()


            # Saving Cropped Image:
            
            cv2.imwrite(str(n)+'.jpg',crop_img)
            n=n+1
    #return crop_img
    
        
        
preprop(imags("C:\\Users\\dhira\\Desktop\\mywork\\Virtual Envs projects\\faces"))
