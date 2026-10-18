import cv2, time

def ConvertingHasing(image_path:str):

    #THE dHASH


    #image will get converted to grayscale and in to OpenCV system
    image_cv = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


    image_width = 9
    image_hight = 8
    #the image will be resized to 9x8 pixels
    image = cv2.resize(image_cv, (image_width, image_hight))
   

    #the dHash list that the program will compare every image with it
    binary_d = []
    
    #we will get every row of the picture
    #image.shape[0] will tell how many rows thare are
    for i in range(image.shape[0]):
        row = image[i]
        
        #the loop will continue until i isnt lenght-1 of row
        for x in range(len(row)-1):

            #we will compere the left number to right and if left is bigger than it goes to 1 else to 0
            if row[x]>row[x+1]:

                binary_d.append(1)
            else:
                binary_d.append(0)
    
    







    #THE aHASH


    #image will get converted to grayscale and in to OpenCV system
    image_cv = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


    image_width = 8
    image_hight = 8
    #the image will be resized to 8x8 pixels
    image = cv2.resize(image_cv, (image_width, image_hight))


    #the aHash list that the program will compare every image with it
    binary_a = []
    list_all_pixals = []


    #the program will get every pixel of the image in one list
    #image.shape[0] will tell how many rows thare are
    for i in range(image.shape[0]):
        #in row will be stored every pixel value of every row
        row = image[i]
        
        #list will have every pixel value of every row
        list_all_pixals.extend(row)
    

    #program will get the avrage brightness of the whole image
    avrage_brightness = sum(int(pixel) for pixel in list_all_pixals) / 64

    #the program will go throue every pixal and check if the pixal is more than avrage brightness(.append(1))
    for i in range (len(list_all_pixals)):

        if list_all_pixals[i] > avrage_brightness:
            binary_a.append(1)
        else:
            binary_a.append(0)


   
    #will sent the list back to the caller
    return binary_d, binary_a
