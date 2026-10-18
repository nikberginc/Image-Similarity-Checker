import os
import shutil

def ADDimage(folder_path, image_path, image_name):

    #program will create the path for the image to get to the file
    destination_path = os.path.join(folder_path, image_name)


    #program will copy the image into the file
    shutil.copy(image_path, destination_path)



