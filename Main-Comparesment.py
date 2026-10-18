from ConvertingHasingFunction import ConvertingHasing
from ImageGetter import getter
from Checker import check_images
import time

print("Program starting...")
time.sleep(0.5)
print("Program running!")
time.sleep(0.5)

map = False


map_checker = input("\n\n\nIf you want to create two folders in documents for it to store the identical and very similar photos type YES: \n\n»» ")

if map_checker[0].lower() == "y":
    map = True
    print("\n\n\nYou will find the folders in C:/Users/.../Documents/Comperesment")
    time.sleep(2)

#user will have to insert a path of the image
image_path = input("\n\nInsert the path to your image here (C:/Users/.../image.png): \n\n»» ")
image_path = image_path.replace("\\", "/")

#user will have to insert a path of the file to compare
compere_check = input("\n\nInsert the path to your file of images to compare here (C:/Users/.../file): \n\n»» ")
compere_check = compere_check.replace("\\", "/")


start_time = time.time() 

#this will get the binary of aHash and dHash of the original image
org_image_binary = ConvertingHasing(image_path)

#program will split the two lists in to two sepret lists
org_image_dHash = org_image_binary[0]
org_image_aHash = org_image_binary[1]


#this will get the list of imiges in the specific file
list_compared_images = getter(compere_check)

#this will compare every image and check if its similar or identical 
results = check_images(org_image_dHash, org_image_aHash, list_compared_images, map)

#the list contains the 
identical = results[0]#identical
very_similar = results[1]#very similar
similar = results[2]#similar
different = results[3]#different


#it will write out the name and similarety of every picture

#x will be every list that is in range
for x in range (len(results)):

    #y will be every item in the list in results
    for y in range (len(results[x])):

        #will print every item from every list
        print("\n\n"+str(results[x][y]))

end_time = time.time()

print("\n\n\nProgram took: "+str(round((end_time-start_time)*1000))+" ms to complete!")