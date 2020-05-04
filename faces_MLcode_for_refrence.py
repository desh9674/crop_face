

import cv2, os,shutil, re


# this program copies specified files from directry tree which mathc the pattern into a specified folder
#create a regx to detect speficic extionsions
# keep it in python folder to work
import os,shutil,re
#os.chdir('C:\\Users\\dhira\\Desktop\\mywork')  ## Change to current directory

myregx = re.compile(r'''^(.*?)          #beforepart anything
                    (\.)                #escape . caracter
                    ((jpg)|(png)|JPEG|jpeg|PNG)$      #extension
                    ''', re.VERBOSE)


# loop walk through foldertree looking for regex in filenames
abspathfiles = []
for folderdir, subfolderdir, fileNameList in os.walk('C:\\Users\\dhira\\Desktop\mywork\\Working Projects\\Faces in images'):
    #print(fileNameList)
    
    for fileName in fileNameList:
        mo = myregx.search(fileName)

        if mo==None:
         continue

        filename = mo.group(1)
        extension= mo.group(3)
        file = filename+extension
        absWrkingdir = folderdir+'\\'+ fileName     #get absolute path of those files
        abspath =absWrkingdir                       # IF REQUIRED os.path.join(absWrkingdir, fileANY)
        abspathfiles.append(abspath)     ## just the list of files scanned


        
        img = cv2.imread(abspath)  # reading the image

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  ## grey image, use if required
        img = cv2.resize(img,(1080,720))  #### This gives the best result, but change all you want or Keep the resolution as it is

        
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   # path to file containing facial features
        #   there are many more files(pre-trained models from Cv2) for various features of face, eyes, noses,etc, located at, Install more as needed
        ####C:\Users\dhira\Desktop\mywork\ML\Datas\cascades ###  features usually located here but, giving path does NOT work
        ## for some reason they do not work directly then simply copy and paste them in current folder 
        faceRect = face_cascade.detectMultiScale2(img,1.3, 5)  # creates a face rectangle on image, scaling parameters are complex, dosent matter keep it as it is,
        #add bracket to see full syntax,  It has already detected face in faceRect, now is only showing part on the image
        #print(faceRect)
        #Show face on image
        for (x,y,w,h) in faceRect[0]:      # syntx
            face = cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),3)  # draw rectancgle 
            cv2.imshow('Img_name', face)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            #k = cv2.waitKey(0)

            
    
#print(abspathfiles)


            








""".

V 0.1


# for color image matrix is 3d and for dark image Numpyarray is 2d matrix
#img = cv2.imread("C:\\Users\\dhira\\Desktop\mywork\\Python Internship data\\IMAGE\\Tarzen.jpg")  # read image as numpyArray
img = cv2.imread("C:\\Users\\dhira\\Desktop\\mywork\\ML\\Datas\\Images\\tom.jpg", 1)   # insrt any image or put zero in video capture mode to find face
#img = cv2.imread("C:\\Users\\dhira\\Desktop\\mywork\\Anacondas\\Images\\Kat.jpg",0) # 0 for gray img, 1 for color image

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


type(img)# 1 channel if greay img, and 3 channel for color image reading


img = cv2.resize(img,(520,400))   # resizze to 200 by 200
#resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))



#### JUST FOR SHOWING THE IMAGE PRESS ANY KEY TO CLOSE   ####
cv2.imshow('Kat', img) #  shows image with given name and varible containing image
cv2.waitKey(0)   # open image for (given no of miliseconds)   # remember to keep this line after the imshow line
cv2.destroyAllWindows()  # then colses the image opened after waiting for given milliseconds
##### REMEMBER TO SHOW THIS LINE AFTER THE IMSHOW LINE  ####

#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # convert image to 
#img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)    # convertst to hsv format s  10110101 grid
#img1 = cv2.getRotationMatrix2D(center=(100,100),angle=30,scale=1)  # get rotationmatrix of this image
#img = cv2.warpAffine(img,img1, dsize=(200,200)) # inputIMAGE, OUTPUTimage,gray matrix_transform( rotates img by 30degree)




#############################              FACE DETECTIONS              ########################

# try commented functions all you want, try different images


#features
#haarcascade_frontalface_default.xml, haarcascade_lowerbody.xml, haarcascade_upperbody.xml, haarcascade_smile.xml

# create a cacadeclassifier object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   # path to file containing facial features
#   there are many more files for various features of face etc, located at, Install more as needed
####D:\Dhairyashil\Software\Anaconda\pkgs\libopencv-3.4.1-h875b8b8_3\Library\etc\lbpcascades  ###  features usually located here but, giving path does NOT work
# Keep the cascade file and python file in same folder to run code successfully

# grey the image
# to check if xml file has been loaded
test = face_cascade.load("haarcascade_frontalface_default.xml")   # comment this if not neede

# search the co-ordinates of image  ( face co-rdinates) Feed grey image
faceRect = face_cascade.detectMultiScale2(img,1.3, 5)          # salefactor=decrease shape value by 5% each time
### very big lession here, keep the xml file in same folder as the python file folder


print(type(faceRect))
print(faceRect)   # prints rectangular co-ordinates of face(shows where the face is)


#faceRect[0][0][1]   # cordanate of face rect, its an array afterall

#adding  the rectangular face box to check  using for loop for any face paterns in the image
#img = cv2.resize(img,(600,600))   # sometimes it does not work if too much resizing is done
for (x,y,w,h) in faceRect[0]:
    img = cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),3)   # rectangle co-ordinates

#rect =  cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

cv2.imshow('Img_name', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

k = cv2.waitKey(0)





##### GONE THROUGH A LOT OF EFFORTS FINDING FOR OVER 6 Hours   # finally got it working  ###########

"""

















