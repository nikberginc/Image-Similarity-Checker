import os


def getter(compere_check):

    compare_list = []
    #goes throu every photo in the selected file
    for filename in os.listdir(compere_check):

        if filename.endswith((".png", ".jpg", ".jpeg", ".bmp")):
            img_path = os.path.join(compere_check, filename)
            compare_list.append(img_path.replace("\\", "/"))
    
    return compare_list