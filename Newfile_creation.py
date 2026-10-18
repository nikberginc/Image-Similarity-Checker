import os

def NEWfile(filename: str):

    #program will get the path of the MAIN documants folder
    documents_path = os.path.join(os.environ['USERPROFILE'], 'Documents')

    #program gets how the file will be called
    folder_name = "Comperesment"

    #it will join the path and the name of the file
    folder_path = os.path.join(documents_path, folder_name)

    #program will check if file already exists and if no it will create it
    if not os.path.exists(folder_path):

        os.makedirs(folder_path)




    #program will get the path of the main documants folder
    documents_path = os.path.join(os.environ['USERPROFILE'], 'Documents', 'Comperesment')

    #program gets how the file will be called
    folder_name = filename

    #it will join the path and the name of the file
    folder_path = os.path.join(documents_path, folder_name)

    #program will check if file already exists and if no it will create it
    if not os.path.exists(folder_path):

        os.makedirs(folder_path)

    return folder_path
       