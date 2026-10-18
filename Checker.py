from ConvertingHasingFunction import ConvertingHasing
from Newfile_creation import NEWfile
from AddImage import ADDimage
import os, time
def check_images(org_image_dHash, org_image_aHash, compared_list, map):

    
    identical = []
    very_similar = []
    different = []
    similar = []

    #the loop will go throu every image and check and stored it into a list if its similar or identical
    for i in range(len(compared_list)):
        compared_image = ConvertingHasing(compared_list[i])

        compared_image_dHash = compared_image[0]
        compared_image_aHash = compared_image[1]

        
        #program gets how many bits are diffrent in the dHash of org image and the image in the file
        distance_dHAsh = sum(a != b for a, b in zip(org_image_dHash, compared_image_dHash))

        #program gets how many bits are diffrent in the aHash of org image and the image in the file
        distance_aHAsh = sum(a != b for a, b in zip(org_image_aHash, compared_image_aHash))


        #program combain all the distances together
        distance = distance_aHAsh + distance_dHAsh

        #program gets how much the images are similar in %    round((1-how many bits are diffrent / all posible bits * 100 for %), 1)
        similarity = round( (  (1 - distance / (len(compared_image_aHash) + len(compared_image_dHash) ) ) * 100 ), 1 )

        #≥96% → same

        #≥ 80% → very similar

        #≥ 60% → similar

        #< 60% → different


        #the program will store image name and how similar it is
        if similarity >= 96:

            if map:
                #program will call the funtion to create a new map
                path = NEWfile("Identical")

                #the program call the function that copys the image into the file
                ADDimage(path, compared_list[i], os.path.basename(compared_list[i]))




            identical.append("Name: "+os.path.basename(compared_list[i])+"   - -  Similarety: "+ str(similarity))

        elif similarity >= 80:
            
            if map:
                #program will call the funtion to create a new map
                path = NEWfile("VerySimilar")


                #the program call the function that copys the image into the file
                ADDimage(path, compared_list[i], os.path.basename(compared_list[i]))




            very_similar.append("Name: "+os.path.basename(compared_list[i])+"  - -   Similarety: "+ str(similarity))

        elif similarity >=60:
            similar.append("Name: "+os.path.basename(compared_list[i])+"  - -   Similarety: "+ str(similarity))
            

        elif similarity < 60:
            different.append("Name: "+os.path.basename(compared_list[i])+"  - -   Similarety: "+ str(similarity))      

    

    


    return identical, very_similar, similar, different

                


