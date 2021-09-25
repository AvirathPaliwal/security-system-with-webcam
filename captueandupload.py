import random
import dropbox
import time
import cv2

start_time = time.time()

def takesnap():
    number = random.randint(1,100)
    #initializing cv2
    vcobj = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True
 
    while(result):
        #read the frames while the camera is on
        ret,frame = vcobj.read()
        img_name = 'img'+str(number)+'.png'
         #cv2.imwrite() method is used to save an image to any storage device 
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result=False
    return img_name
    print('snapshot taken')

     #releases the camera
    vcobj.release()
     #closes all the window that might be opened while this process
    cv2.destroyAllWindows()

def upload_file(img_name):
     access_token = '4xL_15-Tap4AAAAAAAAAAVI_7Ko0iEemn7PxwQ6M_iT8AIfygrI9wM2Nk_LSq4dC'
     file = img_name
     file_from = file
     file_to = '/Images/'+(img_name)
     dbx = dropbox.Dropbox(access_token)
     with open(file_from,'rb') as f:
          #to resolve the path errors last parameter is added
          dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
          print('File uploaded')


def main():
    while(True):
        if((time.time()  -  start_time) >=5 ):
            name = takesnap()
            upload_file(name)

main()
    

